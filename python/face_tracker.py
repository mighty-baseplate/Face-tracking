import cv2
import serial
import time
import mediapipe as mp

# --- Configuration ---
SERIAL_PORT = "COM7"         # Change this to your Arduino port
BAUD_RATE = 9600
WEBCAM_ID = 0
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720
H_SENSITIVITY = 70           # How far (in pixels) the face can move before triggering a turn
MIN_FACE_WIDTH = 5           # Reduced minimum face width for distant detection
MIN_FACE_HEIGHT = 5          # Reduced minimum face height for distant detection

# --- Initialize Arduino Serial ---
arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)
print(f"[INFO] Arduino connected on {SERIAL_PORT}")

# --- Initialize Webcam ---
cap = cv2.VideoCapture(WEBCAM_ID)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

frame_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_center_x = frame_w // 2

print(f"[INFO] Webcam opened: {frame_w}x{frame_h}")

# --- Initialize MediaPipe Face Detection ---
mp_face_detection = mp.solutions.face_detection
# Use model 1 for better long-range detection and lower confidence threshold
face_detection = mp_face_detection.FaceDetection(
    model_selection=1,  # Changed from 0 to 1 for better long-range detection
    min_detection_confidence=0.5  # Lowered from 0.7 to 0.5 for more sensitive detection
)

# --- Initialize backup Haar Cascade detector ---
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# --- Main Loop ---
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Try MediaPipe first
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(frame_rgb)
    
    face_detected = False
    face_center_x = frame_center_x

    if results.detections:
        valid_faces = []
        for detection in results.detections:
            box = detection.location_data.relative_bounding_box
            w = int(box.width * frame_w)
            h = int(box.height * frame_h)
            if w >= MIN_FACE_WIDTH and h >= MIN_FACE_HEIGHT:
                valid_faces.append((detection, w * h))  # Face with area

        if valid_faces:
            # Pick the largest valid face
            best_detection = max(valid_faces, key=lambda item: item[1])[0]
            box = best_detection.location_data.relative_bounding_box

            x = int(box.xmin * frame_w)
            y = int(box.ymin * frame_h)
            w = int(box.width * frame_w)
            h = int(box.height * frame_h)
            face_center_x = x + w // 2
            face_detected = True
            
            # Draw rectangle for visualization
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # cv2.putText(frame, "MediaPipe", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # If MediaPipe fails, try Haar Cascade as backup
    if not face_detected:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Use multiple scale factors for better detection at distance
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.05,  # Smaller scale factor for better small face detection
            minNeighbors=3,    # Reduced from default 5 for more sensitive detection
            minSize=(15, 15),  # Smaller minimum size
            maxSize=(300, 300),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        if len(faces) > 0:
            # Pick the largest face
            largest_face = max(faces, key=lambda f: f[2] * f[3])
            x, y, w, h = largest_face
            face_center_x = x + w // 2
            face_detected = True
            
            # Draw rectangle for visualization
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # cv2.putText(frame, "Haar", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    # Send command to Arduino if face is detected
    if face_detected:
        error_x = face_center_x - frame_center_x

        if error_x > H_SENSITIVITY:
            command = 'R'
        elif error_x < -H_SENSITIVITY:
            command = 'L'
        else:
            command = 'C'

        arduino.write(command.encode())
        
        # Draw face center point
        # cv2.circle(frame, (face_center_x, frame_h // 2), 5, (0, 0, 255), -1)
    else:
        # No face detected, send center command
        arduino.write('C'.encode())

    # Draw center of frame
    # cv2.circle(frame, (frame_center_x, frame_h // 2), 5, (255, 0, 0), -1)
    # cv2.line(frame, (frame_center_x, 0), (frame_center_x, frame_h), (255, 0, 0), 1)

    # Display detection status
    # status = "FACE DETECTED" if face_detected else "NO FACE"
    # cv2.putText(frame, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if face_detected else (0, 0, 255), 2)

    # Display
    cv2.imshow("Face Tracker", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# --- Cleanup ---
cap.release()
arduino.close()
cv2.destroyAllWindows()
print("[INFO] Done.")
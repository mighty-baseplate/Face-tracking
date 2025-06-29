import cv2
import serial
import time
import mediapipe as mp
import argparse
import sys

# --- Configuration ---
BAUD_RATE = 9600
WEBCAM_ID = 0
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720
H_SENSITIVITY = 70
V_SENSITIVITY = 50
MIN_FACE_WIDTH = 5
MIN_FACE_HEIGHT = 5

def initialize_arduino(port, baud_rate):
    """Tries to connect to the Arduino and returns the serial object."""
    try:
        arduino = serial.Serial(port, baud_rate, timeout=1)
        time.sleep(2)
        print(f"[INFO] Arduino connected on {port}")
        return arduino
    except serial.SerialException:
        print(f"[ERROR] Failed to connect to Arduino on port {port}.")
        print("Please check the port and try again.")
        sys.exit(1)

def detect_face(frame, face_detection, face_cascade, frame_w, frame_h):
    """Detects a face and returns its center coordinates (x, y)."""
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(frame_rgb)
    
    face_center_x, face_center_y = None, None

    if results.detections:
        valid_faces = []
        for detection in results.detections:
            box = detection.location_data.relative_bounding_box
            w = int(box.width * frame_w)
            h = int(box.height * frame_h)
            if w >= MIN_FACE_WIDTH and h >= MIN_FACE_HEIGHT:
                valid_faces.append((detection, w * h))

        if valid_faces:
            best_detection = max(valid_faces, key=lambda item: item[1])[0]
            box = best_detection.location_data.relative_bounding_box
            x = int(box.xmin * frame_w)
            y = int(box.ymin * frame_h)
            w = int(box.width * frame_w)
            h = int(box.height * frame_h)
            face_center_x = x + w // 2
            face_center_y = y + h // 2
            return face_center_x, face_center_y, (x, y, w, h)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.05, minNeighbors=3, minSize=(15, 15), maxSize=(300, 300), flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    if len(faces) > 0:
        largest_face = max(faces, key=lambda f: f[2] * f[3])
        x, y, w, h = largest_face
        face_center_x = x + w // 2
        face_center_y = y + h // 2
        return face_center_x, face_center_y, (x, y, w, h)

    return None, None, None

def main(args):
    """Main function to run the face tracking application."""
    arduino = initialize_arduino(args.port, BAUD_RATE)
    cap = cv2.VideoCapture(WEBCAM_ID)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    frame_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_center_x = frame_w // 2
    frame_center_y = frame_h // 2

    print(f"[INFO] Webcam opened: {frame_w}x{frame_h}")

    mp_face_detection = mp.solutions.face_detection
    face_detection = mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    prev_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        face_center_x, face_center_y, face_box = detect_face(frame, face_detection, face_cascade, frame_w, frame_h)

        if face_center_x is not None:
            error_x = face_center_x - frame_center_x
            error_y = face_center_y - frame_center_y

            if error_x > H_SENSITIVITY: arduino.write(b'R')
            elif error_x < -H_SENSITIVITY: arduino.write(b'L')
            else: arduino.write(b'C')

            if error_y > V_SENSITIVITY: arduino.write(b'D')
            elif error_y < -V_SENSITIVITY: arduino.write(b'U')
            else: arduino.write(b'S')

        else:
            arduino.write(b'C')
            arduino.write(b'S')

        if args.visualize:
            if face_box:
                x, y, w, h = face_box
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            curr_time = time.time()
            fps = 1 / (curr_time - prev_time)
            prev_time = curr_time
            cv2.putText(frame, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("Face Tracker", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    arduino.close()
    cv2.destroyAllWindows()
    print("[INFO] Done.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A real-time face tracking system that controls a pan-tilt servo motor with an Arduino.")
    parser.add_argument("--port", default="COM7", help="The serial port of the Arduino.")
    parser.add_argument("--visualize", action="store_true", help="Enable the video feed visualization.")
    args = parser.parse_args()
    main(args)
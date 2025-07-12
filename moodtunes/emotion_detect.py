import cv2
import mediapipe as mp
from deepface import DeepFace

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

def detect_emotion_from_webcam():
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise Exception("Webcam not accessible")

        ret, frame = cap.read()
        cap.release()

        if not ret:
            raise Exception("Could not read frame")

        # Convert to RGB
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect face using MediaPipe
        with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
            results = face_detection.process(img_rgb)

            if not results.detections:
                return "neutral"

            # Get first detected face box
            bboxC = results.detections[0].location_data.relative_bounding_box
            h, w, _ = frame.shape
            x, y, bw, bh = int(bboxC.xmin * w), int(bboxC.ymin * h), int(bboxC.width * w), int(bboxC.height * h)
            face_crop = frame[y:y+bh, x:x+bw]

            # Save and analyze cropped face
            img_path = "face_cropped.jpg"
            cv2.imwrite(img_path, face_crop)

            analysis = DeepFace.analyze(img_path=img_path, actions=['emotion'], enforce_detection=False)
            emotion = analysis[0]['dominant_emotion']

            return emotion.lower()
    except Exception as e:
        print(f"[MediaPipe Error]: {e}")
        return "neutral"

import cv2
import face_recognition
image = face_recognition.load_image_file("face.jpg")
face_locations = face_recognition.face_locations(image)
print(f"Found {len(face_locations)} face(s) in this image.")
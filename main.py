import numpy as np
import face_recognition
import cv2
import os
from PIL import Image

def find_face():
  video_capture = cv2.VideoCapture(0)

  path = './'
  # Store the image file names in a list as long as they are jpgs
  images = [f for f in os.listdir(path) if os.path.splitext(f)[-1] == '.jpg']

  for image in images:
      user_image = face_recognition.load_image_file(image)
      user_face_encoding = face_recognition.face_encodings(user_image)[0]
      
      # Do whatever you need to do with the image



  #joey_image = face_recognition.load_image_file("joey.jpg")
  #joey_face_encoding = face_recognition.face_encodings(joey_image)[0]
  #andrew_image = face_recognition.load_image_file("andrew.png")
  #andrew_face_encoding = face_recognition.face_encodings(andrew_image)[0]

  known_face_encodings = [user_face_encoding]#,andrew_face_encoding
  known_face_names = ["you"] #, and add more

  while True:
    ret, frame = video_capture.read()

    rgb_frame = frame [:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
      matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

      name= "Unknown Face"

      face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

      best_match_index = np.argmin(face_distances)
      if matches[best_match_index]:
        name = known_face_names[best_match_index]
      cv2.rectangle(frame, (left,top),(right, bottom), (0,0,255), 2)

      cv2.rectangle(frame, (left, bottom -35), (right, bottom), (0,0,255), cv2.FILLED)
      font = cv2.FONT_HERSHEY_SIMPLEX
      cv2.putText(frame, name, (left +6, bottom -6), font, 1.0, (255,255,255), 1)

    cv2.imshow('Webcam_facerecognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  video_capture.release()
  cv2.destroyAllWindows()

import face_recognition as fr
import os
import cv2
import numpy as np
from time import sleep

import cv2

def get_image(camera):
 retval, im = camera.read()
 return im
def shoot():
    camera_port = 0
    ramp_frames = 30#for light adjustment
    camera = cv2.VideoCapture(camera_port)
    for i in range(0,ramp_frames):#to adjust light for frames
        temp = get_image(camera)
    print("Taking image...")
    camera_capture = get_image(camera)#to keep the modified image
    #try here
    file ="UserIdentification\\testit.png"
    cv2.imwrite(file, camera_capture)
    del(camera)#to release camera
    cv2.destroyAllWindows()
    cList=classify_face("UserIdentification\\testit.png")
    return cList
def get_encoded_faces():#encodes all faces in the folder and returns a dict{name,imageencoded}
    encoded = {}
    for dirpath, dnames, fnames in os.walk("./UserIdentification"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png") and f!="testit.png":
                face = fr.load_image_file("UserIdentification/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding
    return encoded
def classify_face(im):#to find all faces in an image
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    img = cv2.imread(im, 1)
    
    face_locations = fr.face_locations(img)
    unknown_face_encodings = fr.face_encodings(img, face_locations)
    face_distances = []
    face_names = []
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = fr.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"

        # use the known face with the smallest distance to the new face
        face_distances = fr.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        face_names.append(name)
    return face_names



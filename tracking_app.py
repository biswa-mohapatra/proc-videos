from iris_tracking import iris_track
from device_detection import device_detect
from head_pose_detection import head_pose
from mouth_tracking import track_mouth
import cv2
import mediapipe as mp
import dlib
import numpy as np
import time
import data_sort
import pandas as pd
import os

def start_tracking(video_path):
    try:
        print("Starting detection...")

        # Specify the path from where video needed to be captured
        cap = cv2.VideoCapture(video_path)

        mp_face_mesh = mp.solutions.face_mesh
        face_mesh = mp_face_mesh.FaceMesh(max_num_faces = 1, refine_landmarks = True,min_detection_confidence=0.5, min_tracking_confidence=0.5)

        # |-----------------| Face model for mouth tracking |------------------|
        face_model = dlib.get_frontal_face_detector()
        landmark_model = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


        classes = []
        with open("dnn_model/classes.txt",'r') as f:
            for class_name in f.readlines():
                class_name = class_name.strip()
                classes.append(class_name)

        count = 0

        while cap.isOpened():
            success,frame = cap.read()
            if success:

                # object detection:
                object_detected = device_detect(frame,classes)
                if object_detected == 'cell phone':
                    print("Malpractice :: Cell Phone detected.")
                
                # Head-pose detection:

                head_pose_var = head_pose(frame,face_mesh)

                # tracking iris:
                track_iris = iris_track(frame,face_mesh) 

                # mouth tracking:
                mouth_track = track_mouth(frame,face_model,landmark_model)

                #run video:
                #cv2.imshow("Frame",frame)
                print(f"Head : {head_pose_var}\tIris : {track_iris}\tMouth : {mouth_track}")
                key = cv2.waitKey(1) & 0xFF
                count+=1
                if key == ord('q'):
                    print("Quiting...")
                    break
            else:
                break
        print(f"Total frames covered = {count}")
        cap.release()
        cv2.destroyAllWindows()
        cv2.waitKey(1)
    except Exception:
        raise Exception


    

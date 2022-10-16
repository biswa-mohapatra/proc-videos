from scipy.spatial import distance as dist
from imutils import face_utils
import cv2 as cv2
import mediapipe as mp
import time
import numpy as np

yawn_thresh = 22

# Mouth open calculation:
def cal_yawn(shape):
    top_lip = shape[50:53]
    top_lip = np.concatenate((top_lip, shape[61:64]))
    
    low_lip = shape[56:59]
    low_lip = np.concatenate((low_lip, shape[65:68]))
    
    top_mean = np.mean(top_lip, axis=0)
    low_mean = np.mean(low_lip, axis=0)
    
    distance = dist.euclidean(top_mean,low_mean)
    return distance

def track_mouth(image,face_model,landmark_model):
    try:
        #print("\nTracking mouth...\n")
        faces = face_model(image)
        for face in faces:
            # #------Uncomment the following lines if you also want to detect the face ----------#
            # x1 = face.left()
            # y1 = face.top()
            # x2 = face.right()
            # y2 = face.bottom()
            # # print(face.top())
            # cv2.rectangle(frame,(x1,y1),(x2,y2),(200,0,00),2)


            #----------Detect Landmarks-----------#
            shapes = landmark_model(image,face)
            shape = face_utils.shape_to_np(shapes)

            #-------Detecting/Marking the lower and upper lip--------#
            lip = shape[48:68]
            cv2.drawContours(image,[lip],-1,(0, 165, 255),thickness=3)

            #-------Calculating the lip distance-----#
            lip_dist = cal_yawn(shape)
            # print(lip_dist)
            cv2.imshow("Frame",image)
            if lip_dist > yawn_thresh :
                return "Mouth open"
            else:
                return "Mouth closed"
    except Exception as e:
        raise Exception
# imporing libs:
import cv2 as cv
import numpy as np
import mediapipe as mp
import math


# Calculating ecludeian distance:
def euclidean_distance(point1,point2):
    x1,y1 = point1.ravel()
    x2,y2 = point2.ravel()
    
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance

# Position:
def iris_position(iris_center, right_point,left_point):
    center_to_right = euclidean_distance(iris_center,right_point)
    total_distance = euclidean_distance(right_point,left_point)
    ratio = center_to_right/total_distance
    iris_position = ''
    if ratio <=0.42:
        iris_position = "Right"
    elif ratio > 0.42 and ratio <= 0.57:
        iris_position = "Center"
    else:
        iris_position = "Left"
    
    return iris_position,ratio

def iris_track(frame,face_mesh):
    try:
        # tracking points:

        LEFT_EYE = [362,382,381,380,374,373,390,249,263,466,388,387,386,385,384,398]
        RIGHT_EYE = [33,7,163,144,145,153,154,155,133,173,157,158,159,160,161,246]

        RIGHT_IRIS = [474,475,476,477]  
        LEFT_IRIS = [469,470,471,472]



        L_H_LEFT = [33]
        L_H_RIGHT = [133]

        R_H_LEFT = [362]
        R_H_RIGHT = [263]


        rgb_frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
        img_h,img_w = frame.shape[:2]

        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            mesh_points = np.array([np.multiply([p.x,p.y],[img_w,img_h]).astype(int) for p in results.multi_face_landmarks[0].landmark])
            cv.polylines(frame,[mesh_points[LEFT_EYE]],True,(0,255,0),2,cv.LINE_AA)
            cv.polylines(frame,[mesh_points[RIGHT_EYE]],True,(0,255,0),2,cv.LINE_AA)
            # Iris
            (l_cx,l_cy), l_radius = cv.minEnclosingCircle(mesh_points[LEFT_IRIS])
            (r_cx,r_cy), r_radius = cv.minEnclosingCircle(mesh_points[RIGHT_IRIS])
            
            center_left = np.array([l_cx,l_cy],dtype = np.int32)
            center_right = np.array([r_cx,r_cy],dtype = np.int32)
            
            cv.circle(frame,center_left,int(l_radius),(255,0,255),1,cv.LINE_AA)
            cv.circle(frame,center_right,int(r_radius),(255,0,255),1,cv.LINE_AA)


            # Position:
            iris_pos_right,ratio = iris_position(center_right,mesh_points[R_H_RIGHT][0],mesh_points[R_H_LEFT][0])
            iris_pos_left,ratio = iris_position(center_left,mesh_points[L_H_RIGHT],mesh_points[L_H_LEFT][0])
            
            #print(f"Right eye position :: {iris_pos_right}\tLeft Eye Position :: {iris_pos_left}")
            if iris_pos_right == iris_pos_left:
                return iris_pos_right
            else:
                return "Center"

    except Exception as e:
        raise Exception
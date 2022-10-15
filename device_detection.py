# importing the libraries
import cv2

def device_detect(frame,classes):
    try:
        net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights","dnn_model/yolov4-tiny.cfg")


        model = cv2.dnn_DetectionModel(net)
        model.setInputParams(size=(320,320),scale=1/255)
        #print("\n Detecting modile \n")
        (class_ids,scores,bboxes) = model.detect(frame)
        for class_id,score,bbox in zip(class_ids,scores,bboxes):
            (x,y,w,h) = bbox
            if class_id == 67:
                class_name = classes[class_id]
                cv2.putText(frame,class_name,(x,y-5),cv2.FONT_HERSHEY_PLAIN,5,(200,0,50),2)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(200,0,50),3)
                cv2.imshow("Frame",frame)
                return class_name
    except Exception as e:
        raise e
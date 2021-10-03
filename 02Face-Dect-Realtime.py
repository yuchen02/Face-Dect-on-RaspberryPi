# encoding: utf-8
import cv2
import time
cap=cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
i=0

while(1):
    ret,frame = cap.read()
    image=frame
    start = time.time()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.2, 5)
    for (x, y, w, h) in faces:
        # Create rectangle around faces
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)
    end=time.time()
    fps=1/(end-start)
    fps=round(fps,2)
    cv2.putText(image,'FPS:{}'.format(fps),(15,30),cv2.FONT_ITALIC,0.8,(0,0,255),3)
    k=cv2.waitKey(1)
    if k==27:           #按下ESC退出窗口
        break
    elif k==ord('s'):   #按下s保存图片
        cv2.imwrite('./'+str(i)+'.jpg',frame)
        i+=1
    cv2.imshow("capture", image)
cap.release()
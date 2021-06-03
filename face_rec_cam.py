import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,200)
face_cascade = cv2.CascadeClassifier("C:\\Users\\styli\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

while True:
    s , img = cap.read()
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayimg , scaleFactor=1.78 , minNeighbors=3)

    for x,y,w,h in faces:
        img = cv2.rectangle(img, (x,y),(x+w,y+h),(255,255,0),3)
        cv2.putText(img,'@cool_guy',(x-20,y-20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1)
    cv2.imshow("Video" , img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
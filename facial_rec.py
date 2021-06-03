import cv2

face_cascade = cv2.CascadeClassifier("C:\\Users\\styli\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
img = cv2.imread('sachin.jpg')
#img = cv2.imread('avengers.jpg')
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(grayimg , scaleFactor=1.25 , minNeighbors=2)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y),(x+w,y+h),(255,255,0),3)

resized = cv2.resize(img , (int(img.shape[1]/4),int(img.shape[0]/4)))
cv2.imshow("Face Detection",resized)
#cv2.imshow("Face Detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
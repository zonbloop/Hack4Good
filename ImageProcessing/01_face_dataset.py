"""
Developed by Marcelo Rovai - MJRoBot.org @ 21Feb18
Mod. by Fernando M
"""
import cv2
import os

camera = cv2.VideoCapture(0)
camera.set(3, 650)
camera.set(4, 490)

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Generate id for each person
face_id = input('\n enter user id end press')

count = 0

while(True):

    ret, img = camera.read()
    img = cv2.flip(img, 1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.4, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample and stop video
         break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
camera.release()
cv2.destroyAllWindows()

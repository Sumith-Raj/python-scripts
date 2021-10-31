import cv2
from tkinter.filedialog import askopenfilename

cascade = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade)

cam = cv2.VideoCapture(0)
img_path = askopenfilename()
img = cv2.imread(img_path)
if not img_path:
    while cam:
        a, img = cam.read()
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (23, 34, 56), 2)

        cv2.imshow("win", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
else:
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    print(len(faces))
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (23, 34, 56), 2)

    cv2.imshow("win", img)
    cv2.waitKey(0)



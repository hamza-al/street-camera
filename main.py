import cv2
from tkinter import *
from tkinter import filedialog
root = Tk()
root.title('Select video file')
canvas = Canvas(root, width=460, height=200)
canvas.pack()


def filefind():
    global x
    x = filedialog.askopenfilename(title='Select File', filetypes=(('MP4 files', '*.mp4'), ('All files', '*.*')))
    root.destroy()

info = Label(canvas, text='The file selected will be scanned for pedestrians and cars, which will then \nbe highlighted.')
info.place(relx=0, rely=0.3)

start = Button(canvas, text='Select file',command=filefind)
start.place(relwidth=0.3, relheight=0.1, relx=0.34, rely=0.7)
root.mainloop()

pedestrians = cv2.CascadeClassifier('cascades/data/haarcascade_fullbody.xml')
car = cv2.CascadeClassifier('cascades/data/cars.xml')
cap = cv2.VideoCapture(x)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    pedestrian = pedestrians.detectMultiScale(grey, minNeighbors=2)
    cars = car.detectMultiScale(frame, scaleFactor=2, minNeighbors=3)
    for (x,y,w,h) in pedestrian:
        print(x,y,w,h)
        interest_grey = grey[y:y+h, x:x+w]
        interest = frame[y:y+h, x:x+w]



        colour = (0,0, 255)
        stroke = 2
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0, 255), 2)

    for (x,y,w,h) in cars:
        print(x,y,w,h)
        interest_grey = grey[y:y+h, x:x+w]
        interest = frame[y:y+h, x:x+w]



        colour = (0,0, 255)
        stroke = 2
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0, 0), 2)

    cv2.imshow('Car and pedestrian tracker', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

import cv2
import pathlib
import sys

address = "C:/Users/Jay/Desktop/electron_demo/TWICE.mp4"
print("Python Script Started")

cap = cv2.VideoCapture(address)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

while True:
    print(int(cap.get(cv2.CAP_PROP_POS_FRAMES)), "/", int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
    sys.stdout.flush()

    ret, frame = cap.read()
    if not ret:
        break

    

path = pathlib.Path().absolute()
print("Python Processing Done")
sys.stdout.flush()


import cv2
import pathlib
import sys

address = sys.argv[1]

print("Python processing Started")
print(address)
sys.stdout.flush()
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(address)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# out = cv2.VideoWriter('out.mp4', -1, 25, (frame_width, frame_height))

while True:
    print(int(cap.get(cv2.CAP_PROP_POS_FRAMES)), "/", int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
    sys.stdout.flush()
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )

    # Draw a rectangle around the faces
    # out.write(frame)
# path = pathlib.Path().absolute()
# finaladdr = str(path)+"\out.mp4"
# print(finaladdr)
# sys.stdout.flush()


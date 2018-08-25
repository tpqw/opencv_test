import cv2
import time

cap = cv2.VideoCapture(0)

cap.set(3,1280)
cap.set(4,1024)
time.sleep(2)
cap.set(15, -8.0)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 1)
        cv2.imshow('test', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

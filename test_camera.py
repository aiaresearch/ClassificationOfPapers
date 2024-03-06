import cv2

cap = cv2.VideoCapture(0)


while True:
    ret ,frame = cap.read()
    if ret:
        cv2.imshow("frame", frame)

    if cv2.waitKey(0) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


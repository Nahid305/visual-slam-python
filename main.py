import cv2

cap = cv2.VideoCapture(0)  # 0 for webcam, or use 'video.mp4'

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Video Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import numpy as np

orb = cv2.ORB_create()  # ORB is a fast keypoint detector

ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
prev_kp, prev_des = orb.detectAndCompute(prev_gray, None)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kp, des = orb.detectAndCompute(gray, None)

    frame_with_kp = cv2.drawKeypoints(frame, kp, None, color=(0, 255, 0))

    cv2.imshow("Keypoints", frame_with_kp)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

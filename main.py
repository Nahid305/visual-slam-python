import cv2
import numpy as np

# Initialize video
cap = cv2.VideoCapture(0)  # or use a video path like 'test_video.mp4'

# Initialize ORB detector
orb = cv2.ORB_create()

# Initialize BFMatcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Read the first frame
ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
prev_kp, prev_des = orb.detectAndCompute(prev_gray, None)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kp, des = orb.detectAndCompute(gray, None)

    if des is not None and prev_des is not None:
        matches = bf.match(prev_des, des)
        matches = sorted(matches, key=lambda x: x.distance)

        # Draw top 50 matches
        match_img = cv2.drawMatches(prev_frame, prev_kp, frame, kp, matches[:50], None, flags=2)
        cv2.imshow("Feature Matching", match_img)

        # Update previous frame and keypoints
        prev_frame = frame.copy()
        prev_gray = gray.copy()
        prev_kp, prev_des = kp, des
    else:
        cv2.imshow("Feature Matching", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

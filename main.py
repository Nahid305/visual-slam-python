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

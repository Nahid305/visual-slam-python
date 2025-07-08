def run_slam_on_video(video_source=0):
    import cv2
    import numpy as np

    orb = cv2.ORB_create()
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    K = np.array([[718.0, 0, 320],
                  [0, 718.0, 240],
                  [0,   0,     1]])

    trajectory = np.zeros((600, 600, 3), dtype=np.uint8)
    x, y = 300, 300

    cap = cv2.VideoCapture(video_source)

    ret, prev_frame = cap.read()
    if not ret:
        print("Failed to read video source")
        return None

    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    prev_kp, prev_des = orb.detectAndCompute(prev_gray, None)

    cur_R = np.eye(3)
    cur_t = np.zeros((3, 1))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        kp, des = orb.detectAndCompute(gray, None)

        if prev_des is not None and des is not None:
            matches = bf.match(prev_des, des)
            matches = sorted(matches, key=lambda x: x.distance)

            src_pts = np.float32([prev_kp[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

            E, mask = cv2.findEssentialMat(dst_pts, src_pts, K, method=cv2.RANSAC, prob=0.999, threshold=1.0)

            if E is not None and E.shape == (3, 3):
                _, R, t, mask = cv2.recoverPose(E, dst_pts, src_pts, K)
                cur_t += cur_R @ t
                cur_R = R @ cur_R

                draw_x, draw_y = int(x + cur_t[0][0]*5), int(y + cur_t[2][0]*5)
                cv2.circle(trajectory, (draw_x, draw_y), 1, (0, 255, 0), 2)

            match_img = cv2.drawMatches(prev_frame, prev_kp, frame, kp, matches[:50], None, flags=2)
            cv2.imshow("Feature Matches", match_img)
            cv2.imshow("Trajectory", trajectory)

            prev_frame = frame.copy()
            prev_gray = gray.copy()
            prev_kp, prev_des = kp, des
        else:
            cv2.imshow("Feature Matches", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    cv2.imwrite("trajectory.png", trajectory)
    return "trajectory.png"

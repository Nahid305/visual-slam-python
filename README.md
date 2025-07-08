# 📍 Visual SLAM in Python (Webcam + Video File + Streamlit GUI)

A beginner-friendly Visual SLAM system built using Python and OpenCV. It allows real-time tracking of camera movement and plots the trajectory based on live webcam feed or uploaded video files. Includes a simple Streamlit GUI for demo and interaction.

---

## 🚀 What This Project Does

- Detects keypoints in video frames using ORB (Oriented FAST and Rotated BRIEF)
- Matches those keypoints frame-to-frame using Brute Force Matcher
- Calculates camera motion using the Essential Matrix and pose recovery
- Plots the estimated path (trajectory) of the camera on a blank canvas
- Supports **both live webcam input** and **video upload**
- Simple GUI using **Streamlit** for user-friendly interaction

---

## 📸 Demo

<img src="trajectory_demo.png" width="600"/>

> Optional: [📹 Watch Demo Video](https://youtu.be/your-demo-video-link)

---

## 🧰 Tech Stack

- Python
- OpenCV
- NumPy
- Matplotlib
- Streamlit

---

## 🧠 Real-Life Applications

- Self-driving cars & robot navigation
- AR/VR camera tracking
- Indoor mapping and SLAM research
- Drone flight path tracking

---

## 📂 Project Structure

 visual-slam-python/
│
├── main.py # Core Visual SLAM logic
├── app.py # Streamlit GUI
├── requirements.txt # Dependencies
├── trajectory.png # Output path map (auto-generated)
└── README.md # Project ove

## 🏃 How to Run

1. Install dependencies
```bash
 pip install -r requirements.txt

2.Run core SLAM (webcam)
 python main.py

3.Run with GUI (Streamlit)
 streamlit run app.py

🧪 Test Videos
Use your own phone-recorded video or try open datasets like:

.KITTI Odometry Dataset
.TUM RGB-D Dataset


🙌 Contributions & Feedback
Pull requests and feedback are welcome!
If this helped you, feel free to ⭐ the repo and share it.

📬 Contact
Built by Nahid Ansari
Let’s connect and collaborate!

---


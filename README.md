# 📍 Visual SLAM Web App using Python & Streamlit

A real-time Visual SLAM (Simultaneous Localization and Mapping) demo web app that tracks camera movement using uploaded video files and plots the trajectory of the motion — all running in the cloud!

Built with Python, OpenCV, and Streamlit, this app runs fully in-browser without any local setup.

---

## 🚀 Live Demo

🔗 [Try the Web App](https://your-streamlit-app-link.streamlit.app)  
*(Replace with your actual Streamlit Cloud link)*

---

## 📦 Features

- ✅ Upload any indoor or outdoor camera video
- 🔍 Detects & tracks keypoints frame-to-frame
- 📐 Estimates camera motion using ORB + Essential Matrix
- 🗺️ Draws and displays the camera’s trajectory path
- ☁️ Runs fully in the cloud via Streamlit (no installation needed)

---

## 📽️ What is Visual SLAM?

Visual SLAM helps devices like robot vacuums, drones, or AR apps to understand where they are **and** build a map — using only camera input.

This app simulates that behavior by:
1. Extracting keypoints using ORB
2. Matching features between frames
3. Estimating camera pose from motion
4. Drawing a trajectory map

---

## 🛠️ Tech Stack

- Python 3
- OpenCV (`opencv-python-headless`)
- NumPy
- Streamlit
- Matplotlib

---

## 💻 How to Run Locally

```bash
git clone https://github.com/your-username/visual-slam-python.git
cd visual-slam-python

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
 🧪 Test Video Suggestions
You can record your own indoor phone camera video or download from:

 KITTI Odometry Dataset
 TUM RGB-D Dataset

📂 Project Structure
visual-slam-python/
│
├── app.py               # Streamlit GUI
├── main.py              # Core SLAM logic
├── requirements.txt     # Python dependencies
└── README.md            # Project overview

🙋 About Me
👨‍💻 Developed by Nahid Ansari

Always exploring AI, computer vision, and intelligent systems.

⭐ Like this project?

 Give it a ⭐ on GitHub
 Share your feedback or ideas
 Feel free to fork and contribute!




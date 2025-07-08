import streamlit as st
from main import run_slam_on_video
import tempfile

st.title("Visual SLAM - Live & Video Input")

mode = st.radio("Choose input mode:", ["Live Camera", "Upload Video"])

if mode == "Live Camera":
    if st.button("Start Live SLAM"):
        st.text("Running Visual SLAM on Webcam...")
        output = run_slam_on_video(0)
        if output:
            st.image(output, caption="Live Camera Trajectory", use_column_width=True)

elif mode == "Upload Video":
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi"])
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False) as temp_video:
            temp_video.write(uploaded_file.read())
            temp_path = temp_video.name

        if st.button("Run SLAM on Video"):
            st.text("Processing uploaded video...")
            output = run_slam_on_video(temp_path)
            if output:
                st.image(output, caption="Video Trajectory", use_column_width=True)

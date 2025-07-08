import streamlit as st
import tempfile
from main import run_slam_on_video

st.set_page_config(page_title="Visual SLAM", layout="centered")
st.title("📍 Visual SLAM: Video-Based Camera Trajectory")

st.markdown("Upload a video and see how the camera moves based on Visual SLAM tracking.")

uploaded_file = st.file_uploader("Upload a video file (mp4, avi)", type=["mp4", "avi", "mov"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as temp_video:
        temp_video.write(uploaded_file.read())
        video_path = temp_video.name

    if st.button("Run Visual SLAM"):
        st.info("Processing video... Please wait.")
        output_path = run_slam_on_video(video_path)

        if output_path:
            st.success("Trajectory generated!")
            st.image(output_path, caption="Estimated Camera Trajectory", use_column_width=True)
        else:
            st.error("SLAM processing failed. Try a different video.")

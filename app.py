import streamlit as st
import pyvista as pv
import trimesh
from gtts import gTTS
import os

st.set_page_config(page_title="Farsee AI", layout="wide")

st.title("🌍 Farsee - AI 3D World Explorer")

category = st.selectbox("Select Category", [
    "Mechanics",
    "Human",
    "Animals",
    "Plants",
    "Planets",
    "Rocket",
    "Buildings",
    "Electronics",
    "Mountains"
])

if st.button("Generate 3D Model"):
    mesh = pv.Sphere()
    st.write("3D Model Preview:")
    st.pyvista_chart(mesh)

    explanation = f"This is a 3D model from category {category}"
    tts = gTTS(explanation)
    tts.save("voice.mp3")
    st.audio("voice.mp3")

    st.success("Model Generated Successfully!")

from hashlib import new
from io import BytesIO
import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image

st.title("Traffic Signs Recognition")

# Making sidebar
st.sidebar.title("Menu")

option = st.sidebar.selectbox(
    "Select the options",
    ("Select", "Upload an image", "Settings"),
)

if option != "Select":
    if option == "Upload an image":
        uploaded_file = st.sidebar.file_uploader("Choose a file", type=["jpg", "png"])

    image = Image.new("RGB", (1, 1))
    read = False
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        read = True

    if read:
        st.image(image.resize((2 * image.width, 2 * image.height)))
        read = False

else:
    image = Image.open("../img/ULL.png")
    st.caption(
        "This project is a prototype application on traffic sign recognition for the Final Degree Project."
    )
    image = image.resize((454, 454))
    st.image(image)
    st.caption("Eduardo Expósito Barrera")
    st.caption("Univerrsidad de La Laguna")

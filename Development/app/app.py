from hashlib import new
from io import BytesIO
import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image
from keras.models import load_model
from signs import *
import markdown, codecs

# Load the trained model to classify sign
model = load_model("../model/traffic_classifier.h5")

st.title("Traffic Signs Recognition")

# Making sidebar
st.sidebar.title("Menu")

option = st.sidebar.selectbox(
    "Select the options",
    ("Select", "Upload an image", "Information"),
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
            image = image.resize((30, 30))
            st.image(image.resize((10 * image.width, 10 * image.height)))
            read = False
            if st.button("Classify Image"):
                image = np.expand_dims(image, axis=0)
                image = np.array(image)
                print(image.shape)
                pred = model.predict([image])[0]
                newPred = pred + 1
                newPred = [int(i) for i in newPred]
                maxValue = max(newPred)
                sign = classes[newPred.index(maxValue) + 1]
                print(sign)
                loadingBar = st.progress(0)
                for percentComplete in range(100):
                    time.sleep(0.01)
                    loadingBar.progress(percentComplete + 1)
                st.caption(sign)

    elif option == "Information":
        inputFile = codecs.open(
            "../information/information.md", mode="r", encoding="utf-8"
        )
        text = inputFile.read()
        st.markdown(markdown.markdown(text), unsafe_allow_html=True)

else:
    inputFile = codecs.open("../information/home.md", mode="r", encoding="utf-8")
    text = inputFile.read()
    st.markdown(markdown.markdown(text), unsafe_allow_html=True)

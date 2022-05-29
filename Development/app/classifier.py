# Eduardo Expósito Barrera
# Final Degree Project
# Degree in Computer Engineering (Fourth)
# File containing the signal classifier

import streamlit as st
import numpy as np
import time
from keras.models import load_model
from PIL import Image
from signs import *

# Function that performs recognition of the signal specified by the user
def traffic_signs_recognition(nameFile):
    # Load the trained model to classify sign
    model = load_model("/app/traffic-signs-recognition/Development/models/" + nameFile)

    # File explorer
    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["jpg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image = image.resize((30, 30))
        click = False
        _, centerColum, _ = st.columns(3)
        with centerColum:
            st.image(image.resize((10 * image.width, 10 * image.height)))
            if st.button("Classify Image"):
                click = True
        if click:
            image = np.expand_dims(image, axis=0)
            image = np.array(image)
            print(image.shape)
            try:
                pred = model.predict([image])[0]
                sign = classes[pred.argmax(axis=-1) + 1]
                loadingBar = st.progress(0)
                for percentComplete in range(100):
                    time.sleep(0.01)
                    loadingBar.progress(percentComplete + 1)
                time.sleep(0.2)
                st.caption(
                    'Signal recognized as "'
                    + sign
                    + '" with percentage: '
                    + str(round(np.max(pred) * 100, 2))
                    + "%"
                )
            except ValueError:
                st.caption(
                    "The image you have selected cannot be sorted, choose another image."
                )

import streamlit as st
import numpy as np
import time
from PIL import Image
from keras.models import load_model
from signs import *
import codecs


def recognition(nameFile):
    # Load the trained model to classify sign
    path = "/app/traffic-signs-recognition/Development/models/" + nameFile
    model = load_model(path.encode("utf8", "ignore"))


st.title("Traffic Signs Recognition")

# Making sidebar
st.sidebar.title("Menu")

option = st.sidebar.selectbox(
    "Select an option",
    ("Home", "Upload an image", "Information"),
)

if option != "Home":
    if option == "Upload an image":
        option = st.selectbox("Select an option", ("", "Default model", "Other model"))
        if option == "Default model":
            try:
                nameFile = "traffic_classifier.h5"
                st.caption("The default model is: " + nameFile)

                recognition(nameFile)

            except OSError:
                st.caption("The default model name does not exist.")

        elif option == "Other model":
            file = st.text_input("Model name", "")
            if file != "":
                try:
                    recognition(file)

                except OSError:
                    st.caption("The specified model name does not exist. Instructions:")
                    st.caption('1. The model must be in the "models" directory')
                    st.caption('2. You must put it in the form "Test.h5"')
                    st.caption('3. The model cannot be called "Test.h5"')
            else:
                st.caption('You must put it in the form "Test.h5"')

    elif option == "Information":
        inputFile = codecs.open(
            "/app/traffic-signs-recognition/Development/information/information.md",
            mode="r",
            encoding="utf-8",
        )
        st.markdown(inputFile.read(), unsafe_allow_html=True)

else:
    inputFile = codecs.open(
        "/app/traffic-signs-recognition/Development/information/home.md",
        mode="r",
        encoding="utf-8",
    )
    st.markdown(inputFile.read(), unsafe_allow_html=True)

# Eduardo Expósito Barrera
# Final Degree Project
# Degree in Computer Engineering (Fourth)
# File containing the development of the application

import codecs
import streamlit as st
from classifier import *

# Application title definition
st.title("Traffic Signs Recognition")

# Making sidebar
st.sidebar.title("Menu")

# Definition of sidebar options
option = st.sidebar.selectbox(
    "Select an option",
    ("Home", "Upload an image", "Information"),
)

# Implementation of sidebar options
if option != "Home":
    if option == "Upload an image":
        option = st.selectbox("Select an option", ("", "Default model", "Other model"))
        if option == "Default model":
            try:
                nameFile = "traffic_classifier.h5"
                st.caption("The default model is: " + nameFile)

                traffic_signs_recognition(nameFile)

            except OSError:
                st.caption("The default model name does not exist.")

        elif option == "Other model":
            file = st.text_input("Model name", "")
            if file != "":
                try:
                    traffic_signs_recognition(file)

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

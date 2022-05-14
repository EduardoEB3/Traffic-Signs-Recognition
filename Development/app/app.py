import streamlit as st
import numpy as np
import time
from PIL import Image
from keras.models import load_model
from signs import *
import codecs


def recognition(nameFile):
    # Load the trained model to classify sign
    model = load_model("/app/traffic-signs-recognition/Development/models/" + nameFile)

    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["jpg", "png"])

    image = Image.new("RGB", (1, 1))
    # read = False
    #    read = True
    # if read:
    #   read = False
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        click = False
        _, centerColum, _ = st.columns(3)
        image = image.resize((30, 30))
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

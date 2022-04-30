import streamlit as st
import numpy as np
import time
from PIL import Image
from keras.models import load_model
from signs import *
import markdown, codecs

st.title("Traffic Signs Recognition")

# Making sidebar
st.sidebar.title("Menu")

option = st.sidebar.selectbox(
    "Select the options",
    ("Select", "Upload an image", "Information"),
)

if option != "Select":
    if option == "Upload an image":
        file = st.text_input("Model name", "Test.h5")
        if file != "Test.h5":
            try:
                # Load the trained model to classify sign
                model = load_model("../models/" + file)

                uploaded_file = st.sidebar.file_uploader(
                    "Choose a file", type=["jpg", "png"]
                )

                image = Image.new("RGB", (1, 1))
                read = False
                if uploaded_file is not None:
                    image = Image.open(uploaded_file)
                    read = True

                if read:
                    read = False
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
                            newPred = pred + 1
                            newPred = [int(i) for i in newPred]
                            maxValue = max(newPred)
                            sign = classes[newPred.index(maxValue) + 1]
                            loadingBar = st.progress(0)
                            for percentComplete in range(100):
                                time.sleep(0.01)
                                loadingBar.progress(percentComplete + 1)
                            time.sleep(0.2)
                            st.caption(sign)
                        except ValueError:
                            st.caption(
                                "The image you have selected cannot be sorted, choose another image."
                            )
            except OSError:
                st.caption("The specified model name does not exist. Instructions:")
                st.caption('1. The model must be in the "models" directory')
                st.caption('2. You must put it in the form "Test.h5"')
                st.caption('3. The model cannot be called "Test.h5"')

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

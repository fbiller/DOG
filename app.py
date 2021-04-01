import streamlit as st
import requests
from PIL import Image
from DogBreeds import pre_trained_model
import validators

def get_classification (image) :
    st.image(image,caption='Uploaded image.',use_column_width=True)
    st.write ("")
    st.write("Classifying...")
    label = pre_trained_model(image)
    st.dataframe(label,width=50,height=20)

st.title ("Image classification with mobilenet transfert learning")
st.header("De quelle race est votre chien ?")
st.text ("Téléchargez une photo de chien")

uploaded_file = st.file_uploader("Chose a dog breeds image",type="jpg")
if uploaded_file is not None :
    image = Image.open(uploaded_file)
    st.image(image,caption='Uploaded image.',use_column_width=True)
    st.write ("")
    st.dataframe(label)

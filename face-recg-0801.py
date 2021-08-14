#print("Hello world_0801!")
import streamlit as st
#
import json, os, requests, io
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
#
sub_key = "61491fab089b434eb9415b19344d658e"
face_api_url = "https://facetest0808.cognitiveservices.azure.com/face/v1.0/detect"

#
st.title('顔認識アプリ')
uploaded_file = st.file_uploader("choose an Image...",type ="jpg")
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img,caption='uploded image',use_column_width=True)

print("Hello world_0801!")
import streamlit as st
#
import json, os, requests,io
from PIL import Image, ImageFont
from PIL import ImageDraw

#
sub_key = "61491fab089b434eb9415b19344d658e"
face_api_url = "https://facetest0808.cognitiveservices.azure.com/face/v1.0/detect"

#
st.title('顔認識アプリ')
uploaded_file = st.file_uploader("choose an Image...",type ="jpg")

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    with io.BytesIO()as output:
        img.save(output,format='JPEG')
        binary_img = output.getvalue()
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': "61491fab089b434eb9415b19344d658e"
        }

    params = {
        'returnFaceId': 'true',
        'returnFaceAttributes':'age,gender,headPose,emotion,smile,hair,makeup,glasses'
        }
    res = requests.post(face_api_url, params=params,headers=headers, data=binary_img)
    results = res.json()
    font = ImageFont.truetype("/ipagp.ttf", 30)
#
    for result in results:
        rect = result['faceRectangle']
        age_test = result['faceAttributes']['age']
        emo_test = result['faceAttributes']['emotion']['happiness']
        draw = ImageDraw.Draw(img)
        draw.rectangle([(rect['left'],rect['top']),(rect['left']+rect['width'],rect['top']+rect['height'])], fill=None, outline = 'green', width =5)
        draw.text((rect['left']+10,rect['top']+10),"AGE : "+str(age_test),font=font)
        draw.text((rect['left']+10,rect['top']+rect['height']+10),"Happy Level : "+str(emo_test))

    st.image(img,caption='uploded image',use_column_width=True)

import base64

import streamlit as st
import time

from deepface import DeepFace

from util import format_json
#import streamlit.components.v1 as components

def analyze(io_buffer):
    image_data_url = base64.b64encode(io_buffer.getvalue()) #.decode("utf-8")
    sample_string = 'data:image/jpeg;base64,' + image_data_url.decode("ascii")

    objs = DeepFace.analyze(img_path=sample_string, enforce_detection=False,
                            actions=('age', 'gender', 'race', 'emotion')
                            )

    image_result = format_json(objs,True)

    # Create an image from the decoded data
    # img = Image.open(BytesIO(image_data))
    # # Generate a filename with the current date and time
    # timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    # filename = f"img_{timestamp}.png"  # Change file extension to 'png'
    # print(filename)
    # # Save the image in PNG format
    # file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    # img.save(file_path, 'PNG')
    error_message = 'Image successfully captured'
    # use if you want to display all the images in the folder
    # image_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return image_result
st.set_page_config(layout="wide",page_title="Who Am I?")
#https://www.youtube.com/watch?v=_Um12_OlGgw




st.title("Who am I?")
st.write("Let us figure out your age and other demographics from your image")
st.write("Uplaod an Image or take a picture with camera")

#    img_str = base64.b64encode(io_buffer.getvalue()).decode("utf-8")
#   st.experimental_show(type(img_str))
#   img_tag = f'<img style="border: 1px solid #ddd" src="data:image/jpeg;base64,{img_str}" />'
# components.html(figure_html, height=400)
# import textwrap
# import streamlit.components.v1 as components

tab1,tab2 = st.tabs(["Upload an Image","Take a picture with camera"])
with tab1:
    uploaded_photo = st.file_uploader("Upload a photo", key="photo_upload")
    if uploaded_photo:
        col1,col2=st.columns([1,1])
        with col1:
            st.image(uploaded_photo)
        with col2:
            st.markdown(analyze(uploaded_photo), unsafe_allow_html=True)

            #components.html(analyze(uploaded_photo))

with tab2:
    col1, col2 = st.columns([1, 1])
    with col1:
        camera_photo = st.camera_input("Take a photo", key="photo_camera")
    with col2:
        if camera_photo:
            st.markdown(analyze(camera_photo), unsafe_allow_html=True)

            #components.html(analyze(camera_photo))
            #st.write(analyze(camera_photo))
target_image= None
#base64.b64encode(x).decode('utf-8')
t=None
try:
    t=st.session_state["target_photo"]
except:
    pass
#
# if t:
#     print(t)
#     img = None
#     if t == "photo_upload":
#         img = uploaded_photo
#     elif t == "photo_camera":
#         img = camera_photo
#     if  img:
#         target_image = st.image ( img, use_column_width ="always")


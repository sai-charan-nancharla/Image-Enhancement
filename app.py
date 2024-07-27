import os
import streamlit as st
from PIL import Image
from app_funcs import *
from streamlit_image_comparison import image_comparison



st.set_page_config(
    page_title="ISR using ESRGAN",
    page_icon="💫",
    layout="centered",
    initial_sidebar_state="auto",
)

upload_path = "uploads/"
download_path = "downloads/"


#begin
import base64
import plotly.express as px

df = px.data.iris()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()



img = get_img_as_base64("static/main_banner.png")
img2 = get_img_as_base64("static/bottom_banner.png")

page_bg_img = f"""

<style>
[data-testid="stAppViewContainer"] > .main {{
position: relative;
background-image: url("data:image/png;base64,{img}");
background-size: 140%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}


[data-testid="stHeader"] {{
background: rgba(41,102,160,1);
opacity:0.5;
border-bottom-color: red;
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}

[data-testid="stInfo"]{{
    background: rgba(41,102,160,1);
    opacity:0.8;
}}

[data-testid="stTitle"] {{
            font-size: 36px !important;
        }}

</style>
"""




st.markdown(page_bg_img, unsafe_allow_html=True)


#end

# main_image = Image.open('static/main_banner.png')

# st.image(main_image,use_column_width=True)
st.title(':black[_Image Enhancer_]',anchor=None)

model_name='ESRGAN model ✅'
# model_name = st.radio("Choose Model for Image Super Resolution", ('ESRGAN model ✅', 'PSNR-oriented model ✅'))
# st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.markdown("<b>Upload Image 🚀</b>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["png","jpg","bmp","jpeg"])
if uploaded_file is None:
    st.info('✨ Supports all popular image formats 📷 - PNG, JPG, BMP 😉')
if uploaded_file is not None:
        with open(os.path.join(upload_path,uploaded_file.name),"wb") as f:
            f.write((uploaded_file).getbuffer())
        with st.spinner(f"Working... 💫"):
            uploaded_image = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
            downloaded_image = os.path.abspath(os.path.join(download_path,str("output_"+uploaded_file.name)))

            model = instantiate_model(model_name)
            image_super_resolution(uploaded_image, downloaded_image, model)
            print("Output Image: ", downloaded_image)
            final_image = Image.open(downloaded_image)
            print("Opening ",final_image)
            st.markdown("---")
            st.image(final_image, caption='This is how your final image looks like 😉')
            

          

            # st.markdown("Compare Images")

            # render image-comparison

            container = st.container()
            container.write("Comparison of Images")

            image_comparison(

                img1= uploaded_image,
                img2= downloaded_image,
                label1="Original",
                label2="Enhanced",

            )

                
            with open(downloaded_image, "rb") as file:
                if uploaded_file.name.endswith('.jpg') or uploaded_file.name.endswith('.JPG'):
                    if st.download_button(
                                            label="Download Output Image 📷",
                                            data=file,
                                            file_name=str("output_"+uploaded_file.name),
                                            mime='image/jpg'
                                         ):
                        download_success()

                if uploaded_file.name.endswith('.jpeg') or uploaded_file.name.endswith('.JPEG'):
                    if st.download_button(
                                            label="Download output Image 📷",
                                            data=file,
                                            file_name=str("output_"+uploaded_file.name),
                                            mime='image/jpeg'
                                         ):
                        download_success()

                if uploaded_file.name.endswith('.png') or uploaded_file.name.endswith('.PNG'):
                    if st.download_button(
                                            label="Download output Image 📷",
                                            data=file,
                                            file_name=str("output_"+uploaded_file.name),
                                            mime='image/png'
                                         ):
                        download_success()

                

                if uploaded_file.name.endswith('.bmp') or uploaded_file.name.endswith('.BMP'):
                    if st.download_button(
                                            label="Download output Image 📷",
                                            data=file,
                                            file_name=str("output_"+uploaded_file.name),
                                            mime='image/bmp'
                                         ):
                        download_success()
else:
    st.warning('⚠ Please upload your Image file 😯')

st.markdown("<br><hr><center>Made by Team A2</center><hr>", unsafe_allow_html=True)

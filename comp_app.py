import streamlit as st
from streamlit_image_comparison import image_comparison

st.markdown("Compare Images")

# render image-comparison

container = st.container()
container.write("SAI CHARAN")

image_comparison(

    img1="https://www.webbcompare.com/img/hubble/southern_nebula_700.jpg",
    img2="https://www.webbcompare.com/img/webb/southern_nebula_700.jpg",
    label1="Original",
    label2="Enhanced",

)
import streamlit as st
from PIL import Image
import pandas as pd
from multiapp import MultiApp
        
def load_image(image_file):
    img = Image.open(image_file)
    return img


def fbfa():
    st.title("Images using Facebook FAISS")
    st.write("-------------------------------------------------------------------------------------------------")

    def get_data():
        return pd.read_csv('/home/shreya/Assignment3/Streamlit/Faiss.csv')

    n = 1
    df = get_data()
    images = df['0'].unique()
    st.subheader("Choose an image from the below menu: ")
    pic = st.selectbox('Choices : ', images)
    st.image(pic, width=None)
    z = st.slider('Similar images to be shown?', 1, 10, 1)
    st.subheader("Similar Products")
    for index, row in df.iterrows():
        if row['0'] == pic:
            while n < z + 1:
                st.image(row[str(n)], width=100, caption=row[str(n)])
                n += 1
fbfa()         

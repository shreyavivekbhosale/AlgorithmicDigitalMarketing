#Importing required libraries
from multiapp import MultiApp
import streamlit as st
import pandas as pd


STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""

#Reading the required data


def asearch():
    st.title("Images using Artistic Style Similarity Search Method")
    st.write("-------------------------------------------------------------------------------------------------")
    
    def get_data():
        return pd.read_csv('/home/shreya/Assignment3/Streamlit/Artistic.csv')
       
    n = 1
    df = get_data()
    images = df['0'].unique()
    st.subheader("Choose an image from the dropdown : ")
    pic = st.selectbox('Choices : ', images)
    st.image(pic, width=None)
    
    st.subheader('How Many Images do you want to see?')
    z = st.slider('How many images do you want to see?', 1, 10, 1)
    st.subheader("Similar Products you may want to buy")
    for index, row in df.iterrows():
        if row['0'] == pic:     
            while n < z + 1:
                st.image(row[str(n)], width=100, caption=row[str(n)])
                n += 1

        
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
    st.subheader('Similar images to be shown?')
    z = st.slider('Similar images to be shown?', 1, 10, 1)
    st.subheader("Similar Products")
    for index, row in df.iterrows():
        if row['0'] == pic:
            while n < z + 1:
                st.image(row[str(n)], width=100, caption=row[str(n)])
                n += 1
      

app = MultiApp()
app.add_app("Artistic Style Similarity Search", asearch)
app.add_app("Facebook FAISS", fbfa)
app.run()

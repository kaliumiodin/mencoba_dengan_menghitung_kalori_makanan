import streamlit as st
st.write("Hello, *World!* :sunglasses:")

st.title(":red[MY WEBSITE NEW 2025]")
st.title(":red[_Kaila_ ]is :blue[keren] :sunglasses:")
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

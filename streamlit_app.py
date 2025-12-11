import streamlit as st
st.title(":red[Percobaan Hari Ini]")
st.header(":blue[Penentuan Bilangan Ganjil dan Genap]")
number = int(st.number_input("Insert a number",min_value=0,max_value=10000))
if number%2==1
  st.write("Bilangan",number,"Termasuk bilangan ganjil")
else:
st.write("Bilangan",number,"Termasuk bilangan genap")

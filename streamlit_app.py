import streamlit as st
st.title(":red[Percobaan Hari Ini]")
st.title(":red[Penentuan Bilangan Ganjil dan Genap]")
import streamlit as st

number = int(st.number_input("Insert a number",min_value=None,max_value=None))
if number%2==1
  st.write("Bilangan",number,"Termasuk bilangan ganjil")
else:
st.write("Bilangan",number,"Termasuk bilangan genap")

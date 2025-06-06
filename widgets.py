
"""When you've got the data or model into the state that you want to explore, you can add in widgets like st.slider(), st.button() or st.selectbox(). It's really straightforward — treat widgets as variables:"""



import streamlit as st
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


#Widgets can also be accessed by key, if you choose to specify a string to use as the unique key for the widget:
#

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name
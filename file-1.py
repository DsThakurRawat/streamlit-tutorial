import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'index': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'age of girls': [18, 21, 20, 19, 18, 23, 24, 25, 21, 27],
    'age of boys ': [18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
    'response': ["yes", "yes", "yes", "yes", "no", "yes", "yes", "no", "yes", "no"]
})

st.title("Relationship Age Analysis")
st.write("DataFrame:")
st.write(df)
# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''




x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart
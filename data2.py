import streamlit as st
import numpy as np
import pandas as pd

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)
#This example uses Numpy to generate a random sample, but you can use Pandas DataFrames, Numpy arrays, or plain Python arrays.

#Let's expand on the first example using the Pandas Styler object to highlight some elements in the interactive table.


dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)
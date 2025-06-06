#Draw a line chart
#You can easily add a line chart to your app with st.line_chart(). We'll generate a random sample using Numpy and then chart it.

import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
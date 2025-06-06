##Show progress
#When adding long running computations to an app, you can use st.progress() to display status in real time.

#First, let's import time. We're going to use the time.sleep() method to simulate a long running computation:

import streamlit as st
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
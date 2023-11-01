import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(2080, 3),
     columns=['a', 'b', 'c'])

st.area_chart(chart_data) 

st.write("# Helloooo world!")

st.balloons()
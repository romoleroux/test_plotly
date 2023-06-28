import streamlit as st 
import pandas as pd
import seaborn as sns
import plotly.express as px
import numpy as np
import plotly.figure_factory as ff

df = sns.load_dataset('penguins')

# Page Title
st.title('Ejemplo de uso de st.write()')
st.write('Hola :sumglass :hear')

a = 2**2
st.write(a)
st.write(df.head())
st.markdown('hola como estas')
st.plotly_chart(px.scatter(df, x = 'bill_length_mm', y = 'bill_depth_mm'))

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.title('Data Visualization using streamlit')

def data(nrows):
    data = pd.read_csv('adult.csv',nrows=nrows)
    return data

#Sample data consider for Visualization
data = data(30)
st.subheader('Adult Data in Tabular')
st.write(data)

#bar chart showing the age count
st.subheader('Age')
st.bar_chart(data['age'],width=100, height=400, use_container_width=True)

#line chart diasplaying the capital-gain Vs capital-loss
st.subheader('capital-gain Vs capital-loss')
chart_data = pd.DataFrame(data,columns=['capital-gain','capital-loss'])
st.line_chart(chart_data)

#Area chart showing the age count
st.subheader('Income')
st.area_chart(data['income'])


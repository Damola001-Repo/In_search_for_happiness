import streamlit as st
import plotly.express as px
import pandas as pd

st.header("In search for Happiness")

x_option = st.selectbox("Select the data for X-axis", ['happiness', 'gdp','freedom_to_make_life_choices', 'generosity', 'corruption'])
y_option = st.selectbox("Select the data for Y-axis", ['happiness', 'gdp','freedom_to_make_life_choices', 'generosity', 'corruption'])
st.write("NOTE: The lower the value of corruption the more corrupt the country is")

st.subheader(f"{x_option} and {y_option}")

df = pd.read_csv('happy.csv')

match x_option:
    case 'happiness':
        x = 'happiness'
    case 'gdp':
        x = 'gdp'
    case 'freedom_to_make_life_choices':
        x = 'freedom_to_make_life_choices'
    case 'generosity':
        x = 'generosity'
    case 'corruption':
        x = 'corruption'

match y_option:
    case 'happiness':
        y = 'happiness'
    case 'gdp':
        y = 'gdp'
    case 'freedom_to_make_life_choices':
        y = 'freedom_to_make_life_choices'
    case 'generosity':
        y = 'generosity'
    case 'corruption':
        y = 'corruption'

figure = px.scatter(x = df[x], y = df[y], labels={"x":f"{x}", "y":f"{y}"})
st.plotly_chart(figure)
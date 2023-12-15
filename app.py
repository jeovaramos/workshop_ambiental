"""Launches the main streamlit application."""

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Me formei. E Agora?",
    page_icon="🌎",
)
st.header("Hello, World!")

data = pd.read_csv("data/estudante_escola.csv")
data["estudante"] = data["estudante"].astype(str)
data["escola"] = data["escola"].astype(str)

# st.table(data.dtypes)
st.dataframe(data.head(15))

fig = px.histogram(
    data, x="desempenho", marginal="rug", hover_data=data.columns, nbins=10
)  # box or rug
fig.update_layout(xaxis_range=[0, 100])
st.plotly_chart(fig, theme="streamlit", use_container_width=True)


school = st.select_slider("Selecione a escola", options=data["escola"].unique())
col1, col2 = st.columns(2)
selection = data["escola"] == school
fig1 = px.histogram(
    data[selection], x="desempenho", marginal="rug", hover_data=data.columns, nbins=10
)  # box or rug
fig1.update_layout(xaxis_range=[0, 100])
col1.plotly_chart(fig1, theme="streamlit", use_container_width=True)

texp_mean = round(data[selection]["texp"].mean())
fig2 = px.scatter(
    data[selection], x="horas", y="desempenho", title=f"texp médio = {texp_mean}"
)
fig2.update_layout(yaxis_range=[0, 100])
col2.plotly_chart(fig2, theme="streamlit", use_container_width=True)

fig = px.scatter(data, x="escola", y="desempenho", size="horas", color="texp")
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

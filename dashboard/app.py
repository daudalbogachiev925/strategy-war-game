import os
import requests
import pandas as pd
import streamlit as st
import plotly.express as px

API = os.getenv("API_URL", "http://api:8000")

st.set_page_config(page_title="War Game", layout="wide")
st.title("Strategy War Game")

scenarios = requests.get(f"{API}/api/scenarios").json()
scenario = st.sidebar.selectbox("Сценарий", scenarios)
steps = st.sidebar.slider("Шагов", 20, 200, 60)

if st.sidebar.button("Запустить"):
    r = requests.post(f"{API}/api/run", json={"scenario": scenario}).json()
    hist = pd.DataFrame(r["history"])
    st.session_state["hist"] = hist
    st.session_state["summary"] = r["summary"]

if "hist" in st.session_state:
    hist = st.session_state["hist"]
    s = st.session_state["summary"]

    c1, c2, c3 = st.columns(3)
    c1.metric("Выжило", f"{s['alive']}/{s['total']}")
    c2.metric("Лидер", s["leader"])
    c3.metric("Стратегия лидера", s["leader_strategy"])

    st.subheader("Доли рынка")
    st.plotly_chart(px.area(hist, x="step", y="share", color="company"))

    st.subheader("Cash")
    st.plotly_chart(px.line(hist, x="step", y="cash", color="company"))

    st.subheader("Цены")
    st.plotly_chart(px.line(hist, x="step", y="price", color="company"))

    st.subheader("Качество")
    st.plotly_chart(px.line(hist, x="step", y="quality", color="company"))

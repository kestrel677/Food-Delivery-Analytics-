import os
import io
import json
from datetime import datetime

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Food Delivery Analytics",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded",
)

@st.cache_data
def load_data(path: str = "food_delivery_dataset.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    df["Delivery_person_Age"] = df["Delivery_person_Age"].fillna(df["Delivery_person_Age"].median())
    df["Delivery_person_Ratings"] = df["Delivery_person_Ratings"].fillna(df["Delivery_person_Ratings"].median())
    df["Time_Orderd"] = df["Time_Orderd"].fillna("00:00")
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], format="%d-%m-%Y", errors="coerce")
    df["Delivery_person_Age"] = df["Delivery_person_Age"].astype(int)
    df["multiple_deliveries"] = df["multiple_deliveries"].astype(int)
    df["Time_taken (min)"] = df["Time_taken (min)"].astype(int)
    df["distance_group"] = pd.cut(
        df["distance_km"],
        bins=[0, 5, 10, 15, 25],
        labels=["0-5 km", "5-10 km", "10-15 km", "15-25 km"],
    )
    if "delivery_speed" not in df.columns:
        df["delivery_speed"] = pd.cut(
            df["Time_taken (min)"],
            bins=[0, 20, 30, 120],
            labels=["Fast", "Average", "Slow"]
        ).astype(str)
    return df

try:
    df_raw = load_data()
except FileNotFoundError:
    st.error("❌ **food_delivery_dataset.csv** not found in project root.")
    st.stop()

st.sidebar.header("🔍 Filter Controls")
city_options = sorted(df_raw["City"].dropna().unique().tolist())
vehicle_options = sorted(df_raw["Type_of_vehicle"].dropna().unique().tolist())
weather_options = sorted(df_raw["Weather_conditions"].dropna().unique().tolist())
traffic_options = ["Low", "Medium", "High", "Jam"]
order_options = sorted(df_raw["Type_of_order"].dropna().unique().tolist())

selected_cities = st.sidebar.multiselect("City", city_options, default=city_options)
selected_vehicles = st.sidebar.multiselect("Vehicle Type", vehicle_options, default=vehicle_options)
selected_weather = st.sidebar.multiselect("Weather Conditions", weather_options, default=weather_options)
selected_traffic = st.sidebar.multiselect("Traffic Density", traffic_options, default=traffic_options)
selected_orders = st.sidebar.multiselect("Order Type", order_options, default=order_options)

df = df_raw.copy()
if selected_cities:
    df = df[df["City"].isin(selected_cities)]
if selected_vehicles:
    df = df[df["Type_of_vehicle"].isin(selected_vehicles)]
if selected_weather:
    df = df[df["Weather_conditions"].isin(selected_weather)]
if selected_traffic:
    df = df[df["Road_traffic_density"].isin(selected_traffic)]
if selected_orders:
    df = df[df["Type_of_order"].isin(selected_orders)]

st.title("🍔 Food Delivery Analytics Dashboard")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Deliveries", f"{len(df):,}")
col2.metric("Avg Time (min)", f"{df['Time_taken (min)'].mean():.1f}")
col3.metric("Avg Distance (km)", f"{df['distance_km'].mean():.2f}")
col4.metric("Avg Rating", f"{df['Delivery_person_Ratings'].mean():.2f}")
col5.metric("Avg Courier Age", f"{df['Delivery_person_Age'].mean():.1f}")

st.divider()
st.subheader("📊 Delivery Overview")
st.dataframe(df.head(50), use_container_width=True)

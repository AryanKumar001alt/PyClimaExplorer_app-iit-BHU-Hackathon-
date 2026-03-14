import streamlit as st
import plotly.express as px


def show_time_series(data, lat, lon, title):

    lat_index = st.slider(
        "Latitude Index",
        0,
        len(lat)-1,
        len(lat)//2
    )

    lon_index = st.slider(
        "Longitude Index",
        0,
        len(lon)-1,
        len(lon)//2
    )

    ts = data.isel(
        latitude=lat_index,
        longitude=lon_index
    ).values

    fig = px.line(
        y=ts,
        title=f"{title} Time Series"
    )

    st.plotly_chart(fig, use_container_width=True)
import streamlit as st
import plotly.express as px


def show_map(data, lat, lon, title):

    fig = px.imshow(
        data,
        origin="lower",
        aspect="auto",
        color_continuous_scale="Viridis",
        labels={"color":title}
    )

    fig.update_layout(
        margin=dict(l=0,r=0,t=30,b=0)
    )

    st.plotly_chart(fig, use_container_width=True)
import streamlit as st
import plotly.graph_objects as go


def show_comparison(data, time, lat_idx, lon_idx):

    st.subheader("📊 Climate Comparison")

    series = data[:, lat_idx, lon_idx]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=time,
        y=series,
        mode="lines",
        name="Climate Trend"
    ))

    fig.update_layout(
        title="Climate Comparison",
        xaxis_title="Time",
        yaxis_title="Value"
    )

    st.plotly_chart(fig)
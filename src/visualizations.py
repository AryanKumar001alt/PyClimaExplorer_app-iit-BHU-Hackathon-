import plotly.express as px


def create_map(data, lat, lon, title):

    fig = px.imshow(
        data,
        x=lon,
        y=lat,
        color_continuous_scale="Turbo",
        aspect="auto",
        origin="lower"
    )

    fig.update_layout(
        title=f"{title} Distribution",
        xaxis_title="Longitude",
        yaxis_title="Latitude"
    )

    return fig


def create_time_series(time, values, title):

    fig = px.line(
        x=time,
        y=values,
        markers=True
    )

    fig.update_layout(
        title=f"{title} Trend Over Time",
        xaxis_title="Time",
        yaxis_title=title,
        template="plotly_dark"
    )

    return fig
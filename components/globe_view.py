import streamlit as st
import plotly.graph_objects as go
import numpy as np


def show_3d_globe(lat, lon, data, title):

    # reduce points
    data = data[::3,::3]
    lat = lat[::3]
    lon = lon[::3]

    lon_grid, lat_grid = np.meshgrid(lon,lat)

    fig = go.Figure()

    fig.add_trace(

        go.Scattergeo(

            lon = lon_grid.flatten(),
            lat = lat_grid.flatten(),

            mode = "markers",

            marker = dict(

                size = 3,
                color = data.flatten(),
                colorscale = "Turbo",
                opacity = 0.8

            ),

            hovertemplate =
            "Lat: %{lat}<br>Lon: %{lon}<br>Value: %{marker.color}<extra></extra>"
        )

    )

    fig.update_layout(

        geo = dict(

            projection_type = "orthographic",

            showland = True,
            landcolor = "rgb(230,230,230)",

            showcountries = True,
            countrycolor = "black",

            showocean = True,
            oceancolor = "rgb(10,20,40)"
        ),

        margin = dict(l=0,r=0,t=0,b=0),

        height = 700
    )

    st.plotly_chart(fig,use_container_width=True)
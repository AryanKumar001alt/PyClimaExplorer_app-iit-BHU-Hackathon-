import streamlit as st
import xarray as xr
import numpy as np

from components.map_view import show_map
from components.time_series import show_time_series
from components.globe_view import show_3d_globe
from components.story_mode import show_story


# --------------------------------
# Page Config
# --------------------------------

st.set_page_config(
    page_title="PyClima Explorer",
    page_icon="🌍",
    layout="wide"
)


st.title("🌍 PyClima Explorer")
st.write("Interactive climate dashboard for NetCDF datasets")


# --------------------------------
# Upload dataset
# --------------------------------

uploaded_file = st.file_uploader(
    "Upload NetCDF dataset (.nc)",
    type=["nc"]
)


# --------------------------------
# Dataset Loader
# --------------------------------

@st.cache_data
def load_dataset(file):

    ds = xr.open_dataset(file, engine="h5netcdf")

    # limit timesteps for speed
    if "time" in ds.dims:
        ds = ds.isel(time=slice(0,50))

    # auto compute wind speed
    if "u10" in ds.data_vars and "v10" in ds.data_vars:
        ds["wind_speed"] = np.sqrt(ds["u10"]**2 + ds["v10"]**2)

    return ds


# stop if dataset missing
if uploaded_file is None:
    st.info("Upload a dataset to begin")
    st.stop()


ds = load_dataset(uploaded_file)


# --------------------------------
# Sidebar UI
# --------------------------------

with st.sidebar:

    st.markdown("## 🌍 PyClima Explorer")

    st.markdown(
        """
        **Interactive Climate Data Explorer**

        Visualize temperature, wind and precipitation
        using spatial maps, time series and a 3D globe.
        """
    )

    st.divider()

    st.markdown("### 📂 Dataset")

    st.success("Dataset Loaded")

    st.divider()

    st.markdown("### 🧭 Navigation")

    mode = st.sidebar.radio(
    "Navigation",
    [
        "🌍 Dashboard",
        "🌐 3D Globe",
        "📈 Time Series",
        "📊 Comparison",
        "📖 Story Mode"
    ]
)

    st.divider()

    st.markdown("### 📊 Dataset Stats")

    st.write("Variables:", len(ds.data_vars))
    st.write("Dimensions:", len(ds.dims))

    st.divider()

    st.markdown("### ℹ Instructions")

    st.markdown(
        """
        1 Upload NetCDF dataset  
        2 Select climate variable  
        3 Explore visualizations
        """
    )

    st.caption("Built with Streamlit")


# --------------------------------
# Dataset info
# --------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Dimensions")
    st.write(ds.dims)

with col2:
    st.subheader("Coordinates")
    st.write(list(ds.coords))

with col3:
    st.subheader("Variables")
    st.write(list(ds.data_vars))


# --------------------------------
# Variable Mapping
# --------------------------------

variable_map = {
    "u10": "Wind U Component",
    "v10": "Wind V Component",
    "t2m": "Temperature",
    "tp": "Precipitation",
    "wind_speed": "Wind Speed"
}

variables = list(ds.data_vars)

display_names = [
    variable_map.get(v, v)
    for v in variables
]

selected_display = st.selectbox(
    "Select Climate Variable",
    display_names
)

variable = variables[display_names.index(selected_display)]

data = ds[variable]


# --------------------------------
# Detect time dimension
# --------------------------------

time_dim = None

for dim in data.dims:
    if "time" in dim:
        time_dim = dim

if time_dim is None:
    st.error("No time dimension found")
    st.stop()


# --------------------------------
# Time slider
# --------------------------------

time_index = st.slider(
    "Select Time Index",
    0,
    data.sizes[time_dim]-1,
    0
)

selected_data = data.isel({time_dim: time_index})


# --------------------------------
# Detect latitude longitude
# --------------------------------

lat = ds.coords.get("latitude", ds.coords.get("lat")).values
lon = ds.coords.get("longitude", ds.coords.get("lon")).values


# Downsample for speed
selected_data = selected_data.isel(
    latitude=slice(None,None,2),
    longitude=slice(None,None,2)
)

lat = lat[::2]
lon = lon[::2]


# --------------------------------
# Dashboard
# --------------------------------

if mode == "🌍 Dashboard":

    st.subheader("🌍 Spatial View")

    show_map(
        selected_data.values,
        lat,
        lon,
        selected_display
    )


# --------------------------------
# 3D Globe
# --------------------------------

elif mode == "🌐 3D Globe":

    st.subheader("🌐 3D Climate Globe")

    show_3d_globe(
        lat,
        lon,
        selected_data.values,
        selected_display
    )


# --------------------------------
# Time Series
# --------------------------------

elif mode == "📈 Time Series":

    st.subheader("📈 Time Series")

    show_time_series(
        data,
        lat,
        lon,
        selected_display
    )


# --------------------------------
# Comparison Mode
# --------------------------------

elif mode == "📊 Comparison":

    st.subheader("Dataset Comparison")

    col1,col2 = st.columns(2)

    with col1:
        t1 = st.slider(
            "Time A",
            0,
            data.sizes[time_dim]-1,
            0
        )

    with col2:
        t2 = st.slider(
            "Time B",
            0,
            data.sizes[time_dim]-1,
            10
        )

    col1,col2 = st.columns(2)

    with col1:

        st.write("Dataset A")

        show_map(
            data.isel({time_dim:t1}).values,
            lat,
            lon,
            "A"
        )

    with col2:

        st.write("Dataset B")

        show_map(
            data.isel({time_dim:t2}).values,
            lat,
            lon,
            "B"
        )
elif mode == "📖 Story Mode":

    st.subheader("📖 Climate Story Mode")

    show_story(
        selected_data.values,
        lat,
        lon,
        selected_display
    )

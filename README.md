🌍 PyClima Explorer

Interactive Climate Data Visualization Dashboard for NetCDF datasets built with Streamlit, Plotly, and Xarray.

PyClima Explorer allows users to upload climate datasets and explore them using interactive visualizations such as spatial maps, time series analysis, dataset comparison, and 3D globe views.

🚀 Features
🌍 Spatial Climate Map

Visualize climate variables across geographic coordinates using heatmap maps.

🌐 3D Climate Globe

Interactive globe showing global climate distribution.

📈 Time Series Analysis

Explore how climate variables change over time for a specific location.

📊 Dataset Comparison

Compare two different time steps side-by-side.

📖 Story Mode

Automatically generates insights like:

Average climate values

Maximum and minimum values

Distribution analysis

Climate anomaly hints

⚡ Automatic Processing

The app automatically:

Detects variables in the dataset

Computes wind speed if u10 and v10 exist

Downsamples large datasets for faster visualization

🛠️ Tech Stack

Python

Streamlit

Xarray

NumPy

Pandas

Plotly

NetCDF4

📂 Project Structure
PyClima-Explorer
│
├── app.py                 # Main Streamlit app
├── requirements.txt       # Project dependencies
│
├── components
│   ├── map_view.py        # Spatial heatmap visualization
│   ├── globe_view.py      # 3D globe visualization
│   ├── time_series.py     # Time series analysis
│   ├── story_mode.py      # Story insight generator
│   ├── comparison_view.py # Dataset comparison
│
├── utils
│   ├── processing.py      # Data processing functions
│   ├── visualizations.py  # Plot creation utilities
│
├── style
│   └── style.css          # Custom UI styling
│
└── data
    └── climate_small.nc   # Example compressed dataset

📊 Supported Climate Variables

The app automatically detects variables such as:

Variable	Meaning
u10	Wind U component
v10	Wind V component
t2m	Temperature
tp	Precipitation
wind_speed	Computed wind speed

Wind speed is calculated automatically using:

wind_speed = sqrt(u10² + v10²)

⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/pyclima-explorer.git
cd pyclima-explorer


Install dependencies:

pip install -r requirements.txt

▶️ Run the App

Start the Streamlit application:

streamlit run app.py


Then open your browser at:

http://localhost:8501

📥 Using the App

Upload a NetCDF (.nc) climate dataset.

Select a climate variable.

Choose a visualization mode:

Dashboard

3D Globe

Time Series

Comparison

Story Mode

Explore the climate data interactively.

📦 Dataset Optimization (Optional)

A script is included to compress large NetCDF datasets by:

Reducing precision

Downsampling spatial resolution

Applying NetCDF compression

Run:

python compress_nc.py

🎨 UI Design

The application uses custom CSS styling including:

Dark gradient background

Custom sidebar

Styled metric cards

Modern dashboard UI

🌎 Use Cases

Climate data exploration

Meteorology research

Environmental analytics

Climate change visualization

Educational dashboards

🔮 Future Improvements

Real-time climate APIs

Animation over time

Advanced climate anomaly detection

Satellite dataset support

Multi-dataset comparison

📜 License

MIT License

👨‍💻 Author

Aryan Kumar
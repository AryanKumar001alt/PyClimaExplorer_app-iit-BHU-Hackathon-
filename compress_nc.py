import xarray as xr

# original dataset
ds = xr.open_dataset(r"C:\Users\ARYAN\Downloads\a6ccc01e0ea95c8663a85b06d1012738\climate.nc.nc")

print("Original size dataset loaded")

# reduce precision
for var in ds.data_vars:
    ds[var] = ds[var].astype("float32")

# reduce spatial resolution
if "latitude" in ds.dims:
    ds = ds.isel(latitude=slice(None, None, 2))

if "longitude" in ds.dims:
    ds = ds.isel(longitude=slice(None, None, 2))

# save compressed dataset
ds.to_netcdf(
    "climate_small.nc",
    encoding={var: {"zlib": True, "complevel": 5} for var in ds.data_vars}
)

print("Compressed dataset saved as climate_small.nc")
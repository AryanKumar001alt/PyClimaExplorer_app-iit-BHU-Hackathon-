import xarray as xr

ds = xr.open_dataset("data/data_stream-moda_stepType-avgad.nc")

ds = xr.open_dataset("data/data_stream-moda_stepType-avgua.nc")

print("Dataset info:")
print(ds)

print("\nVariables inside dataset:")
print(list(ds.data_vars))
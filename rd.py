import imdlib as imd
import matplotlib.pyplot as plt
import numpy as np

start_yr = 2017
end_yr = 2017
variable = 'rain' # other options are ('tmin'/ 'tmax')
file_dir = (r'rain') #Path to save the files
data = imd.open_data(variable, start_yr, end_yr,'yearwise', file_dir)
ds = data.get_xarray()
# print(ds.rain.shape)
# print(ds.lon.shape)
# ds = ds.to_dataframe()
# print(ds)

# print(ds)
# print(ds.keys())
# ds = ds.where(ds['rain'] != -999.)

# arr = np.asarray(ds.where(ds['rain'] != -999.))
# print(np.unique(ds['rain'].mean('time')))
ds = ds.where(ds['rain'] != -999.)
ds['rain'].mean('time').plot()
plt.show()
# print(len(ds.lon))
# print(ds)
# print(len(ds.lat))

# lat = 20.03
# lon = 77.23
# data.to_csv('test.csv', lat, lon, file_dir)


# print(ds)

# ds = ds.where(ds['rain'] != -999.) #Remove NaN values
# print(ds['rain'].mean('time'))
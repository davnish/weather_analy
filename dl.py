import imdlib as imd

start_yr = 2017
end_yr = 2018
variable = 'rain' # other options are ('tmin'/ 'tmax')
data = imd.get_data(variable, start_yr, end_yr, fn_format='yearwise')
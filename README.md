# Heathrow_temperature_data

## Some statistics using monthly temperature data from Heathrow airport since 1948

This program reads in temperature data for Heathrow airport from the numpy
binary file heathrow_data.npz, which contains the monthly temperature lows and highs since 1948 (arrays
"month", "year", "tmax", "tmin"). 

It then computes the average <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\overline{x}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\overline{x}" title="\overline{x}" /></a> and standard deviation σ of `tmax` and `tmin` over all months and all
years using whole array operations and the definitions of average and variance:

<a href="https://www.codecogs.com/eqnedit.php?latex=\overline{x}&space;=&space;\frac{1}{N}\sum_{1}^{N}x_{i}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\overline{x}&space;=&space;\frac{1}{N}\sum_{1}^{N}x_{i}" title="\overline{x} = \frac{1}{N}\sum_{1}^{N}x_{i}" /></a> &nbsp; &nbsp; &nbsp; and &nbsp; &nbsp; &nbsp; <a href="https://www.codecogs.com/eqnedit.php?latex=\sigma^{2}&space;=&space;\frac{1}{N-1}\sum_{1}^{N}(x_{i}-\overline{x})^{2}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\sigma^{2}&space;=&space;\frac{1}{N-1}\sum_{1}^{N}(x_{i}-\overline{x})^{2}" title="\sigma^{2} = \frac{1}{N-1}\sum_{1}^{N}(x_{i}-\overline{x})^{2}" /></a>

The results will be later used to fit a linear regression line using the `numpy polyfit` routine to the `tmin`-`tmax` plot.

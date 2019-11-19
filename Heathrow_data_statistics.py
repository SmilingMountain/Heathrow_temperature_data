# -*- coding: utf-8 -*-
"""
@author: Augustin
"""

import numpy as np

infile = np.load("heathrow_data.npz")
print infile
print infile.files

Tmax=infile['tmax']
Tmin=infile['tmin']
Month=infile['month']
Year=infile['year']

Tshape=np.shape(Tmax)
Tlen, =Tshape
tshape=np.shape(Tmin)
tlen, =tshape
Yshape=np.shape(Year)
Ylen, =Yshape
print 'Tlen= ', Tlen, ' tlen= ', tlen, ' number of years: ', Ylen/12

Tavg=(np.sum(Tmax))/Tlen
tavg=(np.sum(Tmin))/tlen
print 'avg(Tmax)= ', Tavg
print 'avg(Tmin)= ', tavg

Tstd=np.sqrt((np.sum((Tmax-Tavg)**2))/(Tlen-1))
tstd=np.sqrt((np.sum((Tmin-tavg)**2))/(tlen-1))
print 'stdev(Tmax)= ', Tstd
print 'stdev(Tmin)= ', tstd

outfile=open("heathrow_weather.txt", "w")
outfile.write("+---------------------------------------------+\n")
outfile.write("|Month|Tmax_avg|Tmax_stdev|Tmin_avg|Tmin_stdev|\n")
outfile.write("|-----+--------+----------+--------+----------|\n")

for k in range(12):
    counter=[12*i+k for i in range(Ylen/12)]
    extracted_max=[Tmax[j] for j in counter]
    Mshape=np.shape(extracted_max)
    Mlen, =Mshape
    Tmax_avg=(np.sum(extracted_max))/Mlen
    Tmax_stdev=np.sqrt((np.sum((extracted_max-Tmax_avg)**2))/(Mlen-1))
    extracted_min=[Tmin[j] for j in counter]
    mshape=np.shape(extracted_min)
    mlen, =mshape
    Tmin_avg=(np.sum(extracted_min))/mlen
    Tmin_stdev=np.sqrt((np.sum((extracted_min-Tmin_avg)**2))/(mlen-1))
    string = " "+str(k+1)+" "+str(Tmax_avg)+" "+str(Tmax_stdev)+" "+str(Tmin_avg)+" "+str(Tmin_stdev)+"\n"
    outfile.write("| %2d  |%8.5f|%9.5f |%8.5f|%9.5f |\n" % (k+1,Tmax_avg,Tmax_stdev,Tmin_avg,Tmin_stdev))
    
outfile.write("+---------------------------------------------+\n")
outfile.close()
print 'Data saved to heathrow_weather.txt'

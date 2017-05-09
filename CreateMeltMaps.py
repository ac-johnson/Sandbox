#Create Melt Maps

from btcube import btcube
import numpy as np
import meltdays
import datetime as dt
from matplotlib import pyplot as plt
import Plotdatafile

yearlist=range(1987,2016)
datatype='19h'

row=130
col=110

setyear=1992

stopthresh=.75
meltthresh=225

plottype = 2

if plottype == 1:
    for year in yearlist:
        cube=btcube(year,datatype)
        cube.createmeltmap(stopthresh,meltthresh)
        Plotdatafile.PlotMeltMap(cube)



cube=btcube(setyear,datatype)
cube.createmeltmap(stopthresh,meltthresh)
Plotdatafile.PlotMeltMap(cube)

meltlen = meltdays()

#plt.figure()
##plt.ion()
#plt.imshow(cubelayer)
#plt.colorbar()



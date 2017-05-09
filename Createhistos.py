#Plot histograms through history

import btcube
import numpy as np
import Plotdatafile

yearlist=range(1987,2015+1)
datatype='19h'

pointrow=121
pointcol=63
#binnum=23

#bins=np.linspace(200,280,27)
bins=np.linspace(145,270,38)


for i in yearlist:
    cube=btcube.btcube(i,datatype)
    Plotdatafile.HistoBT1point(pointrow,pointcol,cube,bins)
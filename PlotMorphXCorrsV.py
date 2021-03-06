from __future__ import division
import numpy
import os
import matplotlib
import matplotlib.pyplot as plt
from currents_visualization import plotCurrentscape

# Cell_Name = 'Gormadoc'
Cell_Name = 'Isembard'
Case = Cell_Name + '_E_COM_I_COM'
dt = 0.1

cmap = matplotlib.cm.get_cmap('jet')
cmap2 = matplotlib.cm.get_cmap('rainbow')

labels0 = ('gKA','gKdrf','gKdrs','gKCa','gM','gL','gNa','gCaT','gCaL','gH')
labels = ('$I_{K_A}$','$I_{Kdrf}$','$I_{Kdrs}$','$I_{KCa}$','$I_M$','$I_L$','$I_{Na}$','$I_{CaT}$','$I_{CaL}$','$I_H$')
r0 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(0) + '_VivoCurrentsS.npy') # Just to initialize r0
r0[6:]=-r0[6:] # Flip inward currents for cross-correlations

# Soma
RecName = '_All_'
RecName2 = '_VivoCurrentsS.npy'
RecName3 = '_VitroCurrentsS.npy'
RecName4 = '_VivoCurrentsD1.npy'
RecName5 = '_VitroCurrentsD1.npy'
RecName6 = '_VivoCurrentsD2.npy'
RecName7 = '_VitroCurrentsD2.npy'
RecName8 = '_VivoCurrentsD3.npy'
RecName9 = '_VitroCurrentsD3.npy'
RecName10 = '_VivoCurrentsD4.npy'
RecName11 = '_VitroCurrentsD4.npy'

RecVName = '_All_'
RecVName2 = '_VivoVoltageS.npy'
RecVName3 = '_VitroVoltageS.npy'
RecVName4 = '_VivoVoltageD1.npy'
RecVName5 = '_VitroVoltageD1.npy'
RecVName6 = '_VivoVoltageD2.npy'
RecVName7 = '_VitroVoltageD2.npy'
RecVName8 = '_VivoVoltageD3.npy'
RecVName9 = '_VitroVoltageD3.npy'
RecVName10 = '_VivoVoltageD4.npy'
RecVName11 = '_VitroVoltageD4.npy'

for y in range(0,5):
    plt.plot(numpy.array([-20,20]),numpy.array([0,0]),color='k',linestyle='dashed',linewidth=1)
    plt.plot(numpy.array([0,0]),numpy.array([-1,1]),color='k',linestyle='dashed',linewidth=1)
    r0 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + RecVName3)
    r1 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + RecVName11)
    a = (r0 - numpy.mean(r0)) / (numpy.std(r0) * len(r0))
    v = (r1 - numpy.mean(r1)) /  numpy.std(r1)
    xcorr = numpy.correlate(a,v,mode='full')
    lags = (numpy.arange(-len(r0)+1, len(r1))*dt)
    plt.plot(lags,xcorr,color=(0,0,0.9,0.9),linestyle='solid')
for y in range(0,5):
    r0 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + RecVName2)
    r1 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + RecVName10)
    a = (r0 - numpy.mean(r0)) / (numpy.std(r0) * len(r0))
    v = (r1 - numpy.mean(r1)) /  numpy.std(r1)
    xcorr = numpy.correlate(a,v,mode='full')
    lags = (numpy.arange(-len(r0)+1, len(r1))*dt)
    plt.plot(lags,xcorr,color=(0.9,0,0,0.9),linestyle='solid')
plt.xticks([])
plt.yticks([])
plt.xlim(-20,20)
plt.ylim(-1,1)
# plt.title('Soma ' + labels[r] + ' X D4 ' + labels[r])
plt.rcParams.update({'font.size': 20})
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_SomaXD4_' + RecVName + '_Voltage.pdf', bbox_inches='tight',dpi=200)
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_SomaXD4_' + RecVName + '_Voltage.png', bbox_inches='tight',dpi=200)
plt.gcf().clear()
plt.cla()
plt.clf()
plt.close()




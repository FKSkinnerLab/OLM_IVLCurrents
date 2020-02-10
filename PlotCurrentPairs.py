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

RecName = '_All_'
RecName2 = '_VivoCurrentsS'
RecName3 = '_VitroCurrentsS'
RecName4 = '_VivoCurrentsD1'
RecName5 = '_VitroCurrentsD1'
RecName6 = '_VivoCurrentsD2'
RecName7 = '_VitroCurrentsD2'
RecName8 = '_VivoCurrentsD3'
RecName9 = '_VitroCurrentsD3'
RecName10 = '_VivoCurrentsD4'
RecName11 = '_VitroCurrentsD4'

tvec = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_tvec.npy')
tvec = tvec/1000 # ms to s
# Soma In Vivo
y=0
r0 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + RecName2 + '.npy')

for r in range(len(r0)):
    for u in range(len(r0)):
        if u <= r:
            # Skip pairs that have already happened or pairs of the same
            continue
        f, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        ax1.plot(tvec,r0[r]*1000,color=(0.4,0,0,0.9),linestyle='solid')
        ax1.set_ylabel(labels[r] + ' (pA)')
        ax2.plot(tvec,r0[u]*1000,color=(0.4,0,0,0.9),linestyle='solid')
        ax2.set_ylabel(labels[u] + ' (pA)')
        # ax2.set_xlabel('Time (s)',fontsize=13)
        ax2.set_xlim(9,10)
        plt.savefig('PlotCurrents_' + Cell_Name + '/' + Cell_Name + RecName2 + '_' + labels0[r] + '_Curr1_' + labels0[u] + '_Curr2.pdf', bbox_inches='tight',dpi=200)
        plt.savefig('PlotCurrents_' + Cell_Name + '/' + Cell_Name + RecName2 + '_' + labels0[r] + '_Curr1_' + labels0[u] + '_Curr2.png', bbox_inches='tight',dpi=200)
        plt.gcf().clear()
        plt.cla()
        plt.clf()
        plt.close()

f, axarr = plt.subplots(5, 2, sharex=True)
axarr[0,0].plot(tvec,r0[0]*1000,color='tab:blue',linestyle='solid')
axarr[0,0].set_ylabel(labels[0] + ' (pA)')
axarr[1,0].plot(tvec,r0[1]*1000,color='tab:orange',linestyle='solid')
axarr[1,0].set_ylabel(labels[1] + ' (pA)')
axarr[2,0].plot(tvec,r0[2]*1000,color='tab:green',linestyle='solid')
axarr[2,0].set_ylabel(labels[2] + ' (pA)')
axarr[3,0].plot(tvec,r0[3]*1000,color='tab:red',linestyle='solid')
axarr[3,0].set_ylabel(labels[3] + ' (pA)')
axarr[4,0].plot(tvec,r0[4]*1000,color='tab:purple',linestyle='solid')
axarr[4,0].set_ylabel(labels[4] + ' (pA)')
axarr[0,1].plot(tvec,r0[5]*1000,color='tab:brown',linestyle='solid')
axarr[0,1].set_ylabel(labels[5] + ' (pA)')
axarr[1,1].plot(tvec,r0[6]*1000,color='tab:pink',linestyle='solid')
axarr[1,1].set_ylabel(labels[6] + ' (pA)')
axarr[2,1].plot(tvec,r0[7]*1000,color='tab:grey',linestyle='solid')
axarr[2,1].set_ylabel(labels[7] + ' (pA)')
axarr[3,1].plot(tvec,r0[8]*1000,color='tab:olive',linestyle='solid')
axarr[3,1].set_ylabel(labels[8] + ' (pA)')
axarr[4,1].plot(tvec,r0[9]*1000,color='tab:cyan',linestyle='solid')
axarr[4,1].set_ylabel(labels[9] + ' (pA)')
axarr[0,0].set_xlim(9,10)
plt.tight_layout()
plt.savefig('PlotCurrents_' + Cell_Name + '/' + Cell_Name + RecName2 + '_AllCurrents.pdf', bbox_inches='tight',dpi=200)
plt.savefig('PlotCurrents_' + Cell_Name + '/' + Cell_Name + RecName2 + '_AllCurrents.png', bbox_inches='tight',dpi=200)
plt.gcf().clear()
plt.cla()
plt.clf()
plt.close()


# Soma In Vitro
y=0
r0 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + RecName3 + '.npy')

for r in range(len(r0)):
    for u in range(len(r0)):
        if u <= r:
            # Skip pairs that have already happened or pairs of the same
            continue
        f, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        ax1.plot(tvec,r0[r]*1000,color=(0,0,0.4,0.9),linestyle='solid')
        ax1.set_ylabel(labels[r] + ' (pA)')
        ax2.plot(tvec,r0[u]*1000,color=(0,0,0.4,0.9),linestyle='solid')
        ax2.set_ylabel(labels[u] + ' (pA)')
        # ax2.set_xlabel('Time (s)',fontsize=13)
        ax2.set_xlim(9,10)
        plt.savefig('PlotCurrents_' + Cell_Name + '/' + Cell_Name + RecName3 + '_' + labels0[r] + '_Curr1_' + labels0[u] + '_Curr2.pdf', bbox_inches='tight',dpi=200)
        plt.savefig('PlotCurrents_' + Cell_Name + '/' + Cell_Name + RecName3 + '_' + labels0[r] + '_Curr1_' + labels0[u] + '_Curr2.png', bbox_inches='tight',dpi=200)
        plt.gcf().clear()
        plt.cla()
        plt.clf()
        plt.close()

f, axarr = plt.subplots(5, 2, sharex=True)
axarr[0,0].plot(tvec,r0[0]*1000,color='tab:blue',linestyle='solid')
axarr[0,0].set_ylabel(labels[0] + ' (pA)')
axarr[1,0].plot(tvec,r0[1]*1000,color='tab:orange',linestyle='solid')
axarr[1,0].set_ylabel(labels[1] + ' (pA)')
axarr[2,0].plot(tvec,r0[2]*1000,color='tab:green',linestyle='solid')
axarr[2,0].set_ylabel(labels[2] + ' (pA)')
axarr[3,0].plot(tvec,r0[3]*1000,color='tab:red',linestyle='solid')
axarr[3,0].set_ylabel(labels[3] + ' (pA)')
axarr[4,0].plot(tvec,r0[4]*1000,color='tab:purple',linestyle='solid')
axarr[4,0].set_ylabel(labels[4] + ' (pA)')
axarr[0,1].plot(tvec,r0[5]*1000,color='tab:brown',linestyle='solid')
axarr[0,1].set_ylabel(labels[5] + ' (pA)')
axarr[1,1].plot(tvec,r0[6]*1000,color='tab:pink',linestyle='solid')
axarr[1,1].set_ylabel(labels[6] + ' (pA)')
axarr[2,1].plot(tvec,r0[7]*1000,color='tab:grey',linestyle='solid')
axarr[2,1].set_ylabel(labels[7] + ' (pA)')
axarr[3,1].plot(tvec,r0[8]*1000,color='tab:olive',linestyle='solid')
axarr[3,1].set_ylabel(labels[8] + ' (pA)')
axarr[4,1].plot(tvec,r0[9]*1000,color='tab:cyan',linestyle='solid')
axarr[4,1].set_ylabel(labels[9] + ' (pA)')
axarr[0,0].set_xlim(9,10)
plt.tight_layout()
plt.savefig('PlotCurrents_' + Cell_Name + '/' + Cell_Name + RecName3 + '_AllCurrents.pdf', bbox_inches='tight',dpi=200)
plt.savefig('PlotCurrents_' + Cell_Name + '/' + Cell_Name + RecName3 + '_AllCurrents.png', bbox_inches='tight',dpi=200)
plt.gcf().clear()
plt.cla()
plt.clf()
plt.close()

# D4 In Vivo
y=0
r0 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + RecName10 + '.npy')

for r in range(len(r0)):
    for u in range(len(r0)):
        if u <= r:
            # Skip pairs that have already happened or pairs of the same
            continue
        f, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        ax1.plot(tvec,r0[r]*1000,color=(0.9,0,0,0.9),linestyle='solid')
        ax1.set_ylabel(labels[r] + ' (pA)')
        ax2.plot(tvec,r0[u]*1000,color=(0.9,0,0,0.9),linestyle='solid')
        ax2.set_ylabel(labels[u] + ' (pA)')
        # ax2.set_xlabel('Time (s)',fontsize=13)
        ax2.set_xlim(9,10)
        plt.savefig('PlotCurrents_' + Cell_Name + '/' + Cell_Name + RecName10 + '_' + labels0[r] + '_Curr1_' + labels0[u] + '_Curr2.pdf', bbox_inches='tight',dpi=200)
        plt.savefig('PlotCurrents_' + Cell_Name + '/' + Cell_Name + RecName10 + '_' + labels0[r] + '_Curr1_' + labels0[u] + '_Curr2.png', bbox_inches='tight',dpi=200)
        plt.gcf().clear()
        plt.cla()
        plt.clf()
        plt.close()

f, axarr = plt.subplots(5, 2, sharex=True)
axarr[0,0].plot(tvec,r0[0]*1000,color='tab:blue',linestyle='solid')
axarr[0,0].set_ylabel(labels[0] + ' (pA)')
axarr[1,0].plot(tvec,r0[1]*1000,color='tab:orange',linestyle='solid')
axarr[1,0].set_ylabel(labels[1] + ' (pA)')
axarr[2,0].plot(tvec,r0[2]*1000,color='tab:green',linestyle='solid')
axarr[2,0].set_ylabel(labels[2] + ' (pA)')
axarr[3,0].plot(tvec,r0[3]*1000,color='tab:red',linestyle='solid')
axarr[3,0].set_ylabel(labels[3] + ' (pA)')
axarr[4,0].plot(tvec,r0[4]*1000,color='tab:purple',linestyle='solid')
axarr[4,0].set_ylabel(labels[4] + ' (pA)')
axarr[0,1].plot(tvec,r0[5]*1000,color='tab:brown',linestyle='solid')
axarr[0,1].set_ylabel(labels[5] + ' (pA)')
axarr[1,1].plot(tvec,r0[6]*1000,color='tab:pink',linestyle='solid')
axarr[1,1].set_ylabel(labels[6] + ' (pA)')
axarr[2,1].plot(tvec,r0[7]*1000,color='tab:grey',linestyle='solid')
axarr[2,1].set_ylabel(labels[7] + ' (pA)')
axarr[3,1].plot(tvec,r0[8]*1000,color='tab:olive',linestyle='solid')
axarr[3,1].set_ylabel(labels[8] + ' (pA)')
axarr[4,1].plot(tvec,r0[9]*1000,color='tab:cyan',linestyle='solid')
axarr[4,1].set_ylabel(labels[9] + ' (pA)')
axarr[0,0].set_xlim(9,10)
plt.tight_layout()
plt.savefig('PlotCurrents_' + Cell_Name + '/' + Cell_Name + RecName10 + '_AllCurrents.pdf', bbox_inches='tight',dpi=200)
plt.savefig('PlotCurrents_' + Cell_Name + '/' + Cell_Name + RecName10 + '_AllCurrents.png', bbox_inches='tight',dpi=200)
plt.gcf().clear()
plt.cla()
plt.clf()
plt.close()

# D4 In Vivo
y=0
r0 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + RecName11 + '.npy')

for r in range(len(r0)):
    for u in range(len(r0)):
        if u <= r:
            # Skip pairs that have already happened or pairs of the same
            continue
        f, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        ax1.plot(tvec,r0[r]*1000,color=(0,0,0.9,0.9),linestyle='solid')
        ax1.set_ylabel(labels[r] + ' (pA)')
        ax2.plot(tvec,r0[u]*1000,color=(0,0,0.9,0.9),linestyle='solid')
        ax2.set_ylabel(labels[u] + ' (pA)')
        # ax2.set_xlabel('Time (s)',fontsize=13)
        ax2.set_xlim(9,10)
        plt.savefig('PlotCurrents_' + Cell_Name + '/' + Cell_Name + RecName11 + '_' + labels0[r] + '_Curr1_' + labels0[u] + '_Curr2.pdf', bbox_inches='tight',dpi=200)
        plt.savefig('PlotCurrents_' + Cell_Name + '/' + Cell_Name + RecName11 + '_' + labels0[r] + '_Curr1_' + labels0[u] + '_Curr2.png', bbox_inches='tight',dpi=200)
        plt.gcf().clear()
        plt.cla()
        plt.clf()
        plt.close()

f, axarr = plt.subplots(5, 2, sharex=True)
axarr[0,0].plot(tvec,r0[0]*1000,color='tab:blue',linestyle='solid')
axarr[0,0].set_ylabel(labels[0] + ' (pA)')
axarr[1,0].plot(tvec,r0[1]*1000,color='tab:orange',linestyle='solid')
axarr[1,0].set_ylabel(labels[1] + ' (pA)')
axarr[2,0].plot(tvec,r0[2]*1000,color='tab:green',linestyle='solid')
axarr[2,0].set_ylabel(labels[2] + ' (pA)')
axarr[3,0].plot(tvec,r0[3]*1000,color='tab:red',linestyle='solid')
axarr[3,0].set_ylabel(labels[3] + ' (pA)')
axarr[4,0].plot(tvec,r0[4]*1000,color='tab:purple',linestyle='solid')
axarr[4,0].set_ylabel(labels[4] + ' (pA)')
axarr[0,1].plot(tvec,r0[5]*1000,color='tab:brown',linestyle='solid')
axarr[0,1].set_ylabel(labels[5] + ' (pA)')
axarr[1,1].plot(tvec,r0[6]*1000,color='tab:pink',linestyle='solid')
axarr[1,1].set_ylabel(labels[6] + ' (pA)')
axarr[2,1].plot(tvec,r0[7]*1000,color='tab:grey',linestyle='solid')
axarr[2,1].set_ylabel(labels[7] + ' (pA)')
axarr[3,1].plot(tvec,r0[8]*1000,color='tab:olive',linestyle='solid')
axarr[3,1].set_ylabel(labels[8] + ' (pA)')
axarr[4,1].plot(tvec,r0[9]*1000,color='tab:cyan',linestyle='solid')
axarr[4,1].set_ylabel(labels[9] + ' (pA)')
axarr[0,0].set_xlim(9,10)
plt.tight_layout()
plt.savefig('PlotCurrents_' + Cell_Name + '/' + Cell_Name + RecName11 + '_AllCurrents.pdf', bbox_inches='tight',dpi=200)
plt.savefig('PlotCurrents_' + Cell_Name + '/' + Cell_Name + RecName11 + '_AllCurrents.png', bbox_inches='tight',dpi=200)
plt.gcf().clear()
plt.cla()
plt.clf()
plt.close()



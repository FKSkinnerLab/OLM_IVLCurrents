### Test Script for a file found in the SDprox2 results from initial Parallel Simulations
from __future__ import division
import numpy
import os
import matplotlib
import matplotlib.pyplot as plt
from currents_visualization import plotCurrentscape

Cell_Name = h.Cell_Name
Case = Cell_Name + '_E_COM_I_COM'

# execfile("CutSpikes_HighConductanceMeasurements.py")
exec(open("CutSpikes_HighConductanceMeasurements.py").read())

# HC Treshold Measurement Values
tstop = 10000 # seconds
font_size = 13
numrerands = 5
# numpy.save('NPYFiles_' + Cell_Name + '/' + Case + 'numrerands.npy',numrerands)

# Examples = zip(LNI_LNE_LIS_LES,HNI_LNE_LIS_LES,LNI_HNE_LIS_LES,HNI_HNE_LIS_LES,LNI_LNE_HIS_LES,HNI_LNE_HIS_LES,LNI_HNE_HIS_LES,HNI_HNE_HIS_LES,LNI_LNE_LIS_HES,HNI_LNE_LIS_HES,LNI_HNE_LIS_HES,HNI_HNE_LIS_HES,LNI_LNE_HIS_HES,HNI_LNE_HIS_HES,LNI_HNE_HIS_HES,HNI_HNE_HIS_HES)
# ExampleStrings = ['LNI_LNE_LIS_LES','HNI_LNE_LIS_LES','LNI_HNE_LIS_LES','HNI_HNE_LIS_LES','LNI_LNE_HIS_LES','HNI_LNE_HIS_LES','LNI_HNE_HIS_LES','HNI_HNE_HIS_LES','LNI_LNE_LIS_HES','HNI_LNE_LIS_HES','LNI_HNE_LIS_HES','HNI_HNE_LIS_HES','LNI_LNE_HIS_HES','HNI_LNE_HIS_HES','LNI_HNE_HIS_HES','HNI_HNE_HIS_HES']
Examples = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_ExampleHCModelParams.npy')
ExampleStrings = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_ExampleHCModelStrings.npy')
ExampleString = ExampleStrings[0]

modfreqs = numpy.array([8,8])
addSUPs = numpy.array([0,1])

numinh = Examples[0][0]
numexc = Examples[1][0]
inhspikes = Examples[2][0]
excspikes = Examples[3][0]

### Setup Recordings and Distance Vector ###
# Colours chosen for shape plotting:
# Soma (i.e. dend[0](0)) = brown
# Dendrite 1 (i.e. d1_comp) = red
# Dendrite 2 (i.e. d2_comp) = blue
# Dendrite 3 (i.e. d3_comp) = green
# Dendrite 4 (i.e. d4_comp) = orange
d1_comp = numpy.int(h.d1_comp)
d2_comp = numpy.int(h.d2_comp)
d3_comp = numpy.int(h.d3_comp)
d4_comp = numpy.int(h.d4_comp)

t_vec = h.Vector()  
t_vec.record(h._ref_t)

v_vec0 = h.Vector()
v_vec0.record(h.soma[0](0.5)._ref_v)

# Site adjacent to soma
v_vec = h.Vector()
v_vec.record(h.dend[0](0)._ref_v)

Ih = h.Vector()
Ih.record(h.dend[0](0)._ref_ih_Ih)

INa = h.Vector()
INa.record(h.dend[0](0)._ref_ina_Nadend)

IKa = h.Vector()
IKa.record(h.dend[0](0)._ref_ik_Ika)

IKdrf = h.Vector()
IKdrf.record(h.dend[0](0)._ref_ik_Ikdrf)

IKdrs = h.Vector()
IKdrs.record(h.dend[0](0)._ref_ik_Ikdrs)

Im = h.Vector()
Im.record(h.dend[0](0)._ref_ik_IM)

IKCa = h.Vector()
IKCa.record(h.dend[0](0)._ref_ik_kca)

ICaL = h.Vector()
ICaL.record(h.dend[0](0)._ref_ica_cal)

ICaT = h.Vector()
ICaT.record(h.dend[0](0)._ref_ica_cat)

Il = h.Vector()
Il.record(h.dend[0](0)._ref_i_passsd)

# Dendrite Recordings 1
v_vecD1 = h.Vector()
v_vecD1.record(h.dend[d1_comp](0)._ref_v)

IhD1 = h.Vector()
IhD1.record(h.dend[d1_comp](0)._ref_ih_Ih)

INaD1 = h.Vector()
INaD1.record(h.dend[d1_comp](0)._ref_ina_Nadend)

IKaD1 = h.Vector()
IKaD1.record(h.dend[d1_comp](0)._ref_ik_Ika)

IKdrfD1 = h.Vector()
IKdrfD1.record(h.dend[d1_comp](0)._ref_ik_Ikdrf)

IKdrsD1 = h.Vector()
IKdrsD1.record(h.dend[d1_comp](0)._ref_ik_Ikdrs)

ImD1 = h.Vector()
ImD1.record(h.dend[d1_comp](0)._ref_ik_IM)

IKCaD1 = h.Vector()
IKCaD1.record(h.dend[d1_comp](0)._ref_ik_kca)

ICaLD1 = h.Vector()
ICaLD1.record(h.dend[d1_comp](0)._ref_ica_cal)

ICaTD1 = h.Vector()
ICaTD1.record(h.dend[d1_comp](0)._ref_ica_cat)

IlD1 = h.Vector()
IlD1.record(h.dend[d1_comp](0)._ref_i_passsd)

# Dendrite Recordings 2
v_vecD2 = h.Vector()
v_vecD2.record(h.dend[d2_comp](0)._ref_v)

IhD2 = h.Vector()
IhD2.record(h.dend[d2_comp](0)._ref_ih_Ih)

INaD2 = h.Vector()
INaD2.record(h.dend[d2_comp](0)._ref_ina_Nadend)

IKaD2 = h.Vector()
IKaD2.record(h.dend[d2_comp](0)._ref_ik_Ika)

IKdrfD2 = h.Vector()
IKdrfD2.record(h.dend[d2_comp](0)._ref_ik_Ikdrf)

IKdrsD2 = h.Vector()
IKdrsD2.record(h.dend[d2_comp](0)._ref_ik_Ikdrs)

ImD2 = h.Vector()
ImD2.record(h.dend[d2_comp](0)._ref_ik_IM)

IKCaD2 = h.Vector()
IKCaD2.record(h.dend[d2_comp](0)._ref_ik_kca)

ICaLD2 = h.Vector()
ICaLD2.record(h.dend[d2_comp](0)._ref_ica_cal)

ICaTD2 = h.Vector()
ICaTD2.record(h.dend[d2_comp](0)._ref_ica_cat)

IlD2 = h.Vector()
IlD2.record(h.dend[d2_comp](0)._ref_i_passsd)

# Dendrite Recordings 3
v_vecD3 = h.Vector()
v_vecD3.record(h.dend[d3_comp](0)._ref_v)

IhD3 = h.Vector()
IhD3.record(h.dend[d3_comp](0)._ref_ih_Ih)

INaD3 = h.Vector()
INaD3.record(h.dend[d3_comp](0)._ref_ina_Nadend)

IKaD3 = h.Vector()
IKaD3.record(h.dend[d3_comp](0)._ref_ik_Ika)

IKdrfD3 = h.Vector()
IKdrfD3.record(h.dend[d3_comp](0)._ref_ik_Ikdrf)

IKdrsD3 = h.Vector()
IKdrsD3.record(h.dend[d3_comp](0)._ref_ik_Ikdrs)

ImD3 = h.Vector()
ImD3.record(h.dend[d3_comp](0)._ref_ik_IM)

IKCaD3 = h.Vector()
IKCaD3.record(h.dend[d3_comp](0)._ref_ik_kca)

ICaLD3 = h.Vector()
ICaLD3.record(h.dend[d3_comp](0)._ref_ica_cal)

ICaTD3 = h.Vector()
ICaTD3.record(h.dend[d3_comp](0)._ref_ica_cat)

IlD3 = h.Vector()
IlD3.record(h.dend[d3_comp](0)._ref_i_passsd)

# Dendrite Recordings 4
v_vecD4 = h.Vector()
v_vecD4.record(h.dend[d4_comp](0)._ref_v)

IhD4 = h.Vector()
IhD4.record(h.dend[d4_comp](0)._ref_ih_Ih)

INaD4 = h.Vector()
INaD4.record(h.dend[d4_comp](0)._ref_ina_Nadend)

IKaD4 = h.Vector()
IKaD4.record(h.dend[d4_comp](0)._ref_ik_Ika)

IKdrfD4 = h.Vector()
IKdrfD4.record(h.dend[d4_comp](0)._ref_ik_Ikdrf)

IKdrsD4 = h.Vector()
IKdrsD4.record(h.dend[d4_comp](0)._ref_ik_Ikdrs)

ImD4 = h.Vector()
ImD4.record(h.dend[d4_comp](0)._ref_ik_IM)

IKCaD4 = h.Vector()
IKCaD4.record(h.dend[d4_comp](0)._ref_ik_kca)

ICaLD4 = h.Vector()
ICaLD4.record(h.dend[d4_comp](0)._ref_ica_cal)

ICaTD4 = h.Vector()
ICaTD4.record(h.dend[d4_comp](0)._ref_ica_cat)

IlD4 = h.Vector()
IlD4.record(h.dend[d4_comp](0)._ref_i_passsd)


labels = ('gKA','gKdrf','gKdrs','gKCa','gM','gL','gNa','gCaT','gCaL','gH')
TStart = 90001
y = 5

# In Vitro - First find slope  and intercept of F/I relationship
h.ic_hold.dur = h.tstop

h.ic_hold.amp = 0.06
output = getMeasures(0,0,0,0,y*6,y,0,0,0)
spikerate1 = output[3]

h.ic_hold.amp = 0.120
output = getMeasures(0,0,0,0,y*6,y,0,0,0)
spikerate2 = output[3]

slope = (spikerate2 - spikerate1)/(0.120-0.06) # Hz/nA
print('Slope = ' + str(slope) + ' Hz/nA')
intercept = spikerate2 - slope*0.120
print('Intercept = ' + str(intercept) + ' Hz')

tvec0 = numpy.array(t_vec)
TStart = 10001
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_tvec.npy',tvec0[TStart:])
TStart = 90001

# Reset holding current and test in vivo
h.ic_hold.amp = 0

IKa_area0 = numpy.zeros(5)
IKdrf_area0 = numpy.zeros(5)
IKdrs_area0 = numpy.zeros(5)
IKCa_area0 = numpy.zeros(5)
Im_area0 = numpy.zeros(5)
Il_area0 = numpy.zeros(5)
INa_area0 = numpy.zeros(5)
ICaT_area0 = numpy.zeros(5)
ICaL_area0 = numpy.zeros(5)
Ih_area0 = numpy.zeros(5)

IKa_area1 = numpy.zeros(5)
IKdrf_area1 = numpy.zeros(5)
IKdrs_area1 = numpy.zeros(5)
IKCa_area1 = numpy.zeros(5)
Im_area1 = numpy.zeros(5)
Il_area1 = numpy.zeros(5)
INa_area1 = numpy.zeros(5)
ICaT_area1 = numpy.zeros(5)
ICaL_area1 = numpy.zeros(5)
Ih_area1 = numpy.zeros(5)

# Dendrite 1
IKa_area0_D1 = numpy.zeros(5)
IKdrf_area0_D1 = numpy.zeros(5)
IKdrs_area0_D1 = numpy.zeros(5)
IKCa_area0_D1 = numpy.zeros(5)
Im_area0_D1 = numpy.zeros(5)
Il_area0_D1 = numpy.zeros(5)
INa_area0_D1 = numpy.zeros(5)
ICaT_area0_D1 = numpy.zeros(5)
ICaL_area0_D1 = numpy.zeros(5)
Ih_area0_D1 = numpy.zeros(5)

IKa_area1_D1 = numpy.zeros(5)
IKdrf_area1_D1 = numpy.zeros(5)
IKdrs_area1_D1 = numpy.zeros(5)
IKCa_area1_D1 = numpy.zeros(5)
Im_area1_D1 = numpy.zeros(5)
Il_area1_D1 = numpy.zeros(5)
INa_area1_D1 = numpy.zeros(5)
ICaT_area1_D1 = numpy.zeros(5)
ICaL_area1_D1 = numpy.zeros(5)
Ih_area1_D1 = numpy.zeros(5)

# Dendrite 2
IKa_area0_D2 = numpy.zeros(5)
IKdrf_area0_D2 = numpy.zeros(5)
IKdrs_area0_D2 = numpy.zeros(5)
IKCa_area0_D2 = numpy.zeros(5)
Im_area0_D2 = numpy.zeros(5)
Il_area0_D2 = numpy.zeros(5)
INa_area0_D2 = numpy.zeros(5)
ICaT_area0_D2 = numpy.zeros(5)
ICaL_area0_D2 = numpy.zeros(5)
Ih_area0_D2 = numpy.zeros(5)

IKa_area1_D2 = numpy.zeros(5)
IKdrf_area1_D2 = numpy.zeros(5)
IKdrs_area1_D2 = numpy.zeros(5)
IKCa_area1_D2 = numpy.zeros(5)
Im_area1_D2 = numpy.zeros(5)
Il_area1_D2 = numpy.zeros(5)
INa_area1_D2 = numpy.zeros(5)
ICaT_area1_D2 = numpy.zeros(5)
ICaL_area1_D2 = numpy.zeros(5)
Ih_area1_D2 = numpy.zeros(5)

# Dendrite 3
IKa_area0_D3 = numpy.zeros(5)
IKdrf_area0_D3 = numpy.zeros(5)
IKdrs_area0_D3 = numpy.zeros(5)
IKCa_area0_D3 = numpy.zeros(5)
Im_area0_D3 = numpy.zeros(5)
Il_area0_D3 = numpy.zeros(5)
INa_area0_D3 = numpy.zeros(5)
ICaT_area0_D3 = numpy.zeros(5)
ICaL_area0_D3 = numpy.zeros(5)
Ih_area0_D3 = numpy.zeros(5)

IKa_area1_D3 = numpy.zeros(5)
IKdrf_area1_D3 = numpy.zeros(5)
IKdrs_area1_D3 = numpy.zeros(5)
IKCa_area1_D3 = numpy.zeros(5)
Im_area1_D3 = numpy.zeros(5)
Il_area1_D3 = numpy.zeros(5)
INa_area1_D3 = numpy.zeros(5)
ICaT_area1_D3 = numpy.zeros(5)
ICaL_area1_D3 = numpy.zeros(5)
Ih_area1_D3 = numpy.zeros(5)

# Dendrite 4
IKa_area0_D4 = numpy.zeros(5)
IKdrf_area0_D4 = numpy.zeros(5)
IKdrs_area0_D4 = numpy.zeros(5)
IKCa_area0_D4 = numpy.zeros(5)
Im_area0_D4 = numpy.zeros(5)
Il_area0_D4 = numpy.zeros(5)
INa_area0_D4 = numpy.zeros(5)
ICaT_area0_D4 = numpy.zeros(5)
ICaL_area0_D4 = numpy.zeros(5)
Ih_area0_D4 = numpy.zeros(5)

IKa_area1_D4 = numpy.zeros(5)
IKdrf_area1_D4 = numpy.zeros(5)
IKdrs_area1_D4 = numpy.zeros(5)
IKCa_area1_D4 = numpy.zeros(5)
Im_area1_D4 = numpy.zeros(5)
Il_area1_D4 = numpy.zeros(5)
INa_area1_D4 = numpy.zeros(5)
ICaT_area1_D4 = numpy.zeros(5)
ICaL_area1_D4 = numpy.zeros(5)
Ih_area1_D4 = numpy.zeros(5)

for y in range(0,5):
    h.ic_hold.amp = 0
    output = getMeasures(numinh,numexc,inhspikes,excspikes,y*6,y,0,0,0)
    spikerate = output[3]
    vvec0 = numpy.array(v_vec)
    vvec00 = numpy.array(v_vec0)
    tvec0 = numpy.array(t_vec)
    
    # Soma
    pIKa = numpy.array(IKa)
    pIKdrf = numpy.array(IKdrf)
    pIKdrs = numpy.array(IKdrs)
    pIKCa = numpy.array(IKCa)
    pIm = numpy.array(Im)
    pIl = numpy.array(Il)
    pINa = numpy.array(INa)
    pICaT = numpy.array(ICaT)
    pICaL = numpy.array(ICaL)
    pIh = numpy.array(Ih)
    
    TStart = 10001
    r0 = [pIKa[TStart:],pIKdrf[TStart:],pIKdrs[TStart:],pIKCa[TStart:],pIm[TStart:],pIl[TStart:],pINa[TStart:],pICaT[TStart:],pICaL[TStart:],pIh[TStart:]]
    numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + '_VivoCurrentsS.npy',r0)
    numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + '_VivoVoltageS.npy',vvec0[TStart:])
    TStart = 90001
    r0 = [pIKa[TStart:],pIKdrf[TStart:],pIKdrs[TStart:],pIKCa[TStart:],pIm[TStart:],pIl[TStart:],pINa[TStart:],pICaT[TStart:],pICaL[TStart:],pIh[TStart:]]
    
    fig0 = plotCurrentscape(vvec0[TStart:], r0)
    fig0.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_seed_' + str(y) + '_Currentscape0Hz.pdf',dpi=500)
    fig0.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_seed_' + str(y) + '_Currentscape0Hz.png',dpi=500)
    fig0.clf()
    plt.close(fig0)
    
    IKa_area1[y] = numpy.trapz(pIKa,t_vec)
    IKdrf_area1[y] = numpy.trapz(pIKdrf,t_vec)
    IKdrs_area1[y] = numpy.trapz(pIKdrs,t_vec)
    IKCa_area1[y] = numpy.trapz(pIKCa,t_vec)
    Im_area1[y] = numpy.trapz(pIm,t_vec)
    Il_area1[y] = numpy.trapz(pIl,t_vec)
    INa_area1[y] = numpy.trapz(pINa,t_vec)
    ICaT_area1[y] = numpy.trapz(pICaT,t_vec)
    ICaL_area1[y] = numpy.trapz(pICaL,t_vec)
    Ih_area1[y] = numpy.trapz(pIh,t_vec)
    
    # Dendrite 1
    vvec0 = numpy.array(v_vecD1)
    pIKa = numpy.array(IKaD1)
    pIKdrf = numpy.array(IKdrfD1)
    pIKdrs = numpy.array(IKdrsD1)
    pIKCa = numpy.array(IKCaD1)
    pIm = numpy.array(ImD1)
    pIl = numpy.array(IlD1)
    pINa = numpy.array(INaD1)
    pICaT = numpy.array(ICaTD1)
    pICaL = numpy.array(ICaLD1)
    pIh = numpy.array(IhD1)
    
    TStart = 10001
    r0 = [pIKa[TStart:],pIKdrf[TStart:],pIKdrs[TStart:],pIKCa[TStart:],pIm[TStart:],pIl[TStart:],pINa[TStart:],pICaT[TStart:],pICaL[TStart:],pIh[TStart:]]
    numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + '_VivoCurrentsD1.npy',r0)
    numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + '_VivoVoltageD1.npy',vvec0[TStart:])
    TStart = 90001
    r0 = [pIKa[TStart:],pIKdrf[TStart:],pIKdrs[TStart:],pIKCa[TStart:],pIm[TStart:],pIl[TStart:],pINa[TStart:],pICaT[TStart:],pICaL[TStart:],pIh[TStart:]]
    
    fig0 = plotCurrentscape(vvec0[TStart:], r0)
    fig0.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_seed_' + str(y) + '_Currentscape0Hz_D1.pdf',dpi=500)
    fig0.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_seed_' + str(y) + '_Currentscape0Hz_D1.png',dpi=500)
    fig0.clf()
    plt.close(fig0)
    
    IKa_area1_D1[y] = numpy.trapz(pIKa,t_vec)
    IKdrf_area1_D1[y] = numpy.trapz(pIKdrf,t_vec)
    IKdrs_area1_D1[y] = numpy.trapz(pIKdrs,t_vec)
    IKCa_area1_D1[y] = numpy.trapz(pIKCa,t_vec)
    Im_area1_D1[y] = numpy.trapz(pIm,t_vec)
    Il_area1_D1[y] = numpy.trapz(pIl,t_vec)
    INa_area1_D1[y] = numpy.trapz(pINa,t_vec)
    ICaT_area1_D1[y] = numpy.trapz(pICaT,t_vec)
    ICaL_area1_D1[y] = numpy.trapz(pICaL,t_vec)
    Ih_area1_D1[y] = numpy.trapz(pIh,t_vec)
    
    # Dendrite 2
    vvec0 = numpy.array(v_vecD2)
    pIKa = numpy.array(IKaD2)
    pIKdrf = numpy.array(IKdrfD2)
    pIKdrs = numpy.array(IKdrsD2)
    pIKCa = numpy.array(IKCaD2)
    pIm = numpy.array(ImD2)
    pIl = numpy.array(IlD2)
    pINa = numpy.array(INaD2)
    pICaT = numpy.array(ICaTD2)
    pICaL = numpy.array(ICaLD2)
    pIh = numpy.array(IhD2)
    
    TStart = 10001
    r0 = [pIKa[TStart:],pIKdrf[TStart:],pIKdrs[TStart:],pIKCa[TStart:],pIm[TStart:],pIl[TStart:],pINa[TStart:],pICaT[TStart:],pICaL[TStart:],pIh[TStart:]]
    numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + '_VivoCurrentsD2.npy',r0)
    numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + '_VivoVoltageD2.npy',vvec0[TStart:])
    TStart = 90001
    r0 = [pIKa[TStart:],pIKdrf[TStart:],pIKdrs[TStart:],pIKCa[TStart:],pIm[TStart:],pIl[TStart:],pINa[TStart:],pICaT[TStart:],pICaL[TStart:],pIh[TStart:]]
    
    fig0 = plotCurrentscape(vvec0[TStart:], r0)
    fig0.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_seed_' + str(y) + '_Currentscape0Hz_D2.pdf',dpi=500)
    fig0.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_seed_' + str(y) + '_Currentscape0Hz_D2.png',dpi=500)
    fig0.clf()
    plt.close(fig0)
    
    IKa_area1_D2[y] = numpy.trapz(pIKa,t_vec)
    IKdrf_area1_D2[y] = numpy.trapz(pIKdrf,t_vec)
    IKdrs_area1_D2[y] = numpy.trapz(pIKdrs,t_vec)
    IKCa_area1_D2[y] = numpy.trapz(pIKCa,t_vec)
    Im_area1_D2[y] = numpy.trapz(pIm,t_vec)
    Il_area1_D2[y] = numpy.trapz(pIl,t_vec)
    INa_area1_D2[y] = numpy.trapz(pINa,t_vec)
    ICaT_area1_D2[y] = numpy.trapz(pICaT,t_vec)
    ICaL_area1_D2[y] = numpy.trapz(pICaL,t_vec)
    Ih_area1_D2[y] = numpy.trapz(pIh,t_vec)
    
    # Dendrite 3
    vvec0 = numpy.array(v_vecD3)
    pIKa = numpy.array(IKaD3)
    pIKdrf = numpy.array(IKdrfD3)
    pIKdrs = numpy.array(IKdrsD3)
    pIKCa = numpy.array(IKCaD3)
    pIm = numpy.array(ImD3)
    pIl = numpy.array(IlD3)
    pINa = numpy.array(INaD3)
    pICaT = numpy.array(ICaTD3)
    pICaL = numpy.array(ICaLD3)
    pIh = numpy.array(IhD3)
    
    TStart = 10001
    r0 = [pIKa[TStart:],pIKdrf[TStart:],pIKdrs[TStart:],pIKCa[TStart:],pIm[TStart:],pIl[TStart:],pINa[TStart:],pICaT[TStart:],pICaL[TStart:],pIh[TStart:]]
    numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + '_VivoCurrentsD3.npy',r0)
    numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + '_VivoVoltageD3.npy',vvec0[TStart:])
    TStart = 90001
    r0 = [pIKa[TStart:],pIKdrf[TStart:],pIKdrs[TStart:],pIKCa[TStart:],pIm[TStart:],pIl[TStart:],pINa[TStart:],pICaT[TStart:],pICaL[TStart:],pIh[TStart:]]
    
    fig0 = plotCurrentscape(vvec0[TStart:], r0)
    fig0.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_seed_' + str(y) + '_Currentscape0Hz_D3.pdf',dpi=500)
    fig0.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_seed_' + str(y) + '_Currentscape0Hz_D3.png',dpi=500)
    fig0.clf()
    plt.close(fig0)
    
    IKa_area1_D3[y] = numpy.trapz(pIKa,t_vec)
    IKdrf_area1_D3[y] = numpy.trapz(pIKdrf,t_vec)
    IKdrs_area1_D3[y] = numpy.trapz(pIKdrs,t_vec)
    IKCa_area1_D3[y] = numpy.trapz(pIKCa,t_vec)
    Im_area1_D3[y] = numpy.trapz(pIm,t_vec)
    Il_area1_D3[y] = numpy.trapz(pIl,t_vec)
    INa_area1_D3[y] = numpy.trapz(pINa,t_vec)
    ICaT_area1_D3[y] = numpy.trapz(pICaT,t_vec)
    ICaL_area1_D3[y] = numpy.trapz(pICaL,t_vec)
    Ih_area1_D3[y] = numpy.trapz(pIh,t_vec)
    
    # Dendrite 4
    vvec0 = numpy.array(v_vecD4)
    pIKa = numpy.array(IKaD4)
    pIKdrf = numpy.array(IKdrfD4)
    pIKdrs = numpy.array(IKdrsD4)
    pIKCa = numpy.array(IKCaD4)
    pIm = numpy.array(ImD4)
    pIl = numpy.array(IlD4)
    pINa = numpy.array(INaD4)
    pICaT = numpy.array(ICaTD4)
    pICaL = numpy.array(ICaLD4)
    pIh = numpy.array(IhD4)
    
    TStart = 10001
    r0 = [pIKa[TStart:],pIKdrf[TStart:],pIKdrs[TStart:],pIKCa[TStart:],pIm[TStart:],pIl[TStart:],pINa[TStart:],pICaT[TStart:],pICaL[TStart:],pIh[TStart:]]
    numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + '_VivoCurrentsD4.npy',r0)
    numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + '_VivoVoltageD4.npy',vvec0[TStart:])
    TStart = 90001
    r0 = [pIKa[TStart:],pIKdrf[TStart:],pIKdrs[TStart:],pIKCa[TStart:],pIm[TStart:],pIl[TStart:],pINa[TStart:],pICaT[TStart:],pICaL[TStart:],pIh[TStart:]]
    
    fig0 = plotCurrentscape(vvec0[TStart:], r0)
    fig0.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_seed_' + str(y) + '_Currentscape0Hz_D4.pdf',dpi=500)
    fig0.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_seed_' + str(y) + '_Currentscape0Hz_D4.png',dpi=500)
    fig0.clf()
    plt.close(fig0)
    
    IKa_area1_D4[y] = numpy.trapz(pIKa,t_vec)
    IKdrf_area1_D4[y] = numpy.trapz(pIKdrf,t_vec)
    IKdrs_area1_D4[y] = numpy.trapz(pIKdrs,t_vec)
    IKCa_area1_D4[y] = numpy.trapz(pIKCa,t_vec)
    Im_area1_D4[y] = numpy.trapz(pIm,t_vec)
    Il_area1_D4[y] = numpy.trapz(pIl,t_vec)
    INa_area1_D4[y] = numpy.trapz(pINa,t_vec)
    ICaT_area1_D4[y] = numpy.trapz(pICaT,t_vec)
    ICaL_area1_D4[y] = numpy.trapz(pICaL,t_vec)
    Ih_area1_D4[y] = numpy.trapz(pIh,t_vec)
    
    # Now find holding current to generate same spike rate as in vivo and test in vitro case
    h.ic_hold.amp = (spikerate-intercept)/slope
    print('Holding Current = ' + str(h.ic_hold.amp) + ' nA')
    output = getMeasures(0,0,0,0,y*6,y,0,0,0)
    
    vvec0 = numpy.array(v_vec)
    vvec00 = numpy.array(v_vec0)
    tvec0 = numpy.array(t_vec)
    
    pIKa = numpy.array(IKa)
    pIKdrf = numpy.array(IKdrf)
    pIKdrs = numpy.array(IKdrs)
    pIKCa = numpy.array(IKCa)
    pIm = numpy.array(Im)
    pIl = numpy.array(Il)
    pINa = numpy.array(INa)
    pICaT = numpy.array(ICaT)
    pICaL = numpy.array(ICaL)
    pIh = numpy.array(Ih)
    
    TStart = 10001
    r0 = [pIKa[TStart:],pIKdrf[TStart:],pIKdrs[TStart:],pIKCa[TStart:],pIm[TStart:],pIl[TStart:],pINa[TStart:],pICaT[TStart:],pICaL[TStart:],pIh[TStart:]]
    numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + '_VitroCurrentsS.npy',r0)
    numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + '_VitroVoltageS.npy',vvec0[TStart:])
    TStart = 90001
    r0 = [pIKa[TStart:],pIKdrf[TStart:],pIKdrs[TStart:],pIKCa[TStart:],pIm[TStart:],pIl[TStart:],pINa[TStart:],pICaT[TStart:],pICaL[TStart:],pIh[TStart:]]
    
    fig0 = plotCurrentscape(vvec0[TStart:], r0)
    fig0.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_seed_' + str(y) + '_CurrentscapeInVitro.pdf',dpi=500)
    fig0.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_seed_' + str(y) + '_CurrentscapeInVitro.png',dpi=500)
    fig0.clf()
    plt.close(fig0)
    
    IKa_area0[y] = numpy.trapz(pIKa,t_vec)
    IKdrf_area0[y] = numpy.trapz(pIKdrf,t_vec)
    IKdrs_area0[y] = numpy.trapz(pIKdrs,t_vec)
    IKCa_area0[y] = numpy.trapz(pIKCa,t_vec)
    Im_area0[y] = numpy.trapz(pIm,t_vec)
    Il_area0[y] = numpy.trapz(pIl,t_vec)
    INa_area0[y] = numpy.trapz(pINa,t_vec)
    ICaT_area0[y] = numpy.trapz(pICaT,t_vec)
    ICaL_area0[y] = numpy.trapz(pICaL,t_vec)
    Ih_area0[y] = numpy.trapz(pIh,t_vec)
    
    # Dendrite 1
    vvec0 = numpy.array(v_vecD1)
    pIKa = numpy.array(IKaD1)
    pIKdrf = numpy.array(IKdrfD1)
    pIKdrs = numpy.array(IKdrsD1)
    pIKCa = numpy.array(IKCaD1)
    pIm = numpy.array(ImD1)
    pIl = numpy.array(IlD1)
    pINa = numpy.array(INaD1)
    pICaT = numpy.array(ICaTD1)
    pICaL = numpy.array(ICaLD1)
    pIh = numpy.array(IhD1)
    
    TStart = 10001
    r0 = [pIKa[TStart:],pIKdrf[TStart:],pIKdrs[TStart:],pIKCa[TStart:],pIm[TStart:],pIl[TStart:],pINa[TStart:],pICaT[TStart:],pICaL[TStart:],pIh[TStart:]]
    numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + '_VitroCurrentsD1.npy',r0)
    numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + '_VitroVoltageD1.npy',vvec0[TStart:])
    TStart = 90001
    r0 = [pIKa[TStart:],pIKdrf[TStart:],pIKdrs[TStart:],pIKCa[TStart:],pIm[TStart:],pIl[TStart:],pINa[TStart:],pICaT[TStart:],pICaL[TStart:],pIh[TStart:]]
    
    fig0 = plotCurrentscape(vvec0[TStart:], r0)
    fig0.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_seed_' + str(y) + '_CurrentscapeInVitro_D1.pdf',dpi=500)
    fig0.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_seed_' + str(y) + '_CurrentscapeInVitro_D1.png',dpi=500)
    fig0.clf()
    plt.close(fig0)
    
    IKa_area0_D1[y] = numpy.trapz(pIKa,t_vec)
    IKdrf_area0_D1[y] = numpy.trapz(pIKdrf,t_vec)
    IKdrs_area0_D1[y] = numpy.trapz(pIKdrs,t_vec)
    IKCa_area0_D1[y] = numpy.trapz(pIKCa,t_vec)
    Im_area0_D1[y] = numpy.trapz(pIm,t_vec)
    Il_area0_D1[y] = numpy.trapz(pIl,t_vec)
    INa_area0_D1[y] = numpy.trapz(pINa,t_vec)
    ICaT_area0_D1[y] = numpy.trapz(pICaT,t_vec)
    ICaL_area0_D1[y] = numpy.trapz(pICaL,t_vec)
    Ih_area0_D1[y] = numpy.trapz(pIh,t_vec)
    
    # Dendrite 2
    vvec0 = numpy.array(v_vecD2)
    pIKa = numpy.array(IKaD2)
    pIKdrf = numpy.array(IKdrfD2)
    pIKdrs = numpy.array(IKdrsD2)
    pIKCa = numpy.array(IKCaD2)
    pIm = numpy.array(ImD2)
    pIl = numpy.array(IlD2)
    pINa = numpy.array(INaD2)
    pICaT = numpy.array(ICaTD2)
    pICaL = numpy.array(ICaLD2)
    pIh = numpy.array(IhD2)
    
    TStart = 10001
    r0 = [pIKa[TStart:],pIKdrf[TStart:],pIKdrs[TStart:],pIKCa[TStart:],pIm[TStart:],pIl[TStart:],pINa[TStart:],pICaT[TStart:],pICaL[TStart:],pIh[TStart:]]
    numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + '_VitroCurrentsD2.npy',r0)
    numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + '_VitroVoltageD2.npy',vvec0[TStart:])
    TStart = 90001
    r0 = [pIKa[TStart:],pIKdrf[TStart:],pIKdrs[TStart:],pIKCa[TStart:],pIm[TStart:],pIl[TStart:],pINa[TStart:],pICaT[TStart:],pICaL[TStart:],pIh[TStart:]]
    
    fig0 = plotCurrentscape(vvec0[TStart:], r0)
    fig0.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_seed_' + str(y) + '_CurrentscapeInVitro_D2.pdf',dpi=500)
    fig0.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_seed_' + str(y) + '_CurrentscapeInVitro_D2.png',dpi=500)
    fig0.clf()
    plt.close(fig0)
    
    IKa_area0_D2[y] = numpy.trapz(pIKa,t_vec)
    IKdrf_area0_D2[y] = numpy.trapz(pIKdrf,t_vec)
    IKdrs_area0_D2[y] = numpy.trapz(pIKdrs,t_vec)
    IKCa_area0_D2[y] = numpy.trapz(pIKCa,t_vec)
    Im_area0_D2[y] = numpy.trapz(pIm,t_vec)
    Il_area0_D2[y] = numpy.trapz(pIl,t_vec)
    INa_area0_D2[y] = numpy.trapz(pINa,t_vec)
    ICaT_area0_D2[y] = numpy.trapz(pICaT,t_vec)
    ICaL_area0_D2[y] = numpy.trapz(pICaL,t_vec)
    Ih_area0_D2[y] = numpy.trapz(pIh,t_vec)
    
    # Dendrite 3
    vvec0 = numpy.array(v_vecD3)
    pIKa = numpy.array(IKaD3)
    pIKdrf = numpy.array(IKdrfD3)
    pIKdrs = numpy.array(IKdrsD3)
    pIKCa = numpy.array(IKCaD3)
    pIm = numpy.array(ImD3)
    pIl = numpy.array(IlD3)
    pINa = numpy.array(INaD3)
    pICaT = numpy.array(ICaTD3)
    pICaL = numpy.array(ICaLD3)
    pIh = numpy.array(IhD3)
    
    TStart = 10001
    r0 = [pIKa[TStart:],pIKdrf[TStart:],pIKdrs[TStart:],pIKCa[TStart:],pIm[TStart:],pIl[TStart:],pINa[TStart:],pICaT[TStart:],pICaL[TStart:],pIh[TStart:]]
    numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + '_VitroCurrentsD3.npy',r0)
    numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + '_VitroVoltageD3.npy',vvec0[TStart:])
    TStart = 90001
    r0 = [pIKa[TStart:],pIKdrf[TStart:],pIKdrs[TStart:],pIKCa[TStart:],pIm[TStart:],pIl[TStart:],pINa[TStart:],pICaT[TStart:],pICaL[TStart:],pIh[TStart:]]
    
    fig0 = plotCurrentscape(vvec0[TStart:], r0)
    fig0.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_seed_' + str(y) + '_CurrentscapeInVitro_D3.pdf',dpi=500)
    fig0.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_seed_' + str(y) + '_CurrentscapeInVitro_D3.png',dpi=500)
    fig0.clf()
    plt.close(fig0)
    
    IKa_area0_D3[y] = numpy.trapz(pIKa,t_vec)
    IKdrf_area0_D3[y] = numpy.trapz(pIKdrf,t_vec)
    IKdrs_area0_D3[y] = numpy.trapz(pIKdrs,t_vec)
    IKCa_area0_D3[y] = numpy.trapz(pIKCa,t_vec)
    Im_area0_D3[y] = numpy.trapz(pIm,t_vec)
    Il_area0_D3[y] = numpy.trapz(pIl,t_vec)
    INa_area0_D3[y] = numpy.trapz(pINa,t_vec)
    ICaT_area0_D3[y] = numpy.trapz(pICaT,t_vec)
    ICaL_area0_D3[y] = numpy.trapz(pICaL,t_vec)
    Ih_area0_D3[y] = numpy.trapz(pIh,t_vec)
    
    # Dendrite 4
    vvec0 = numpy.array(v_vecD4)
    pIKa = numpy.array(IKaD4)
    pIKdrf = numpy.array(IKdrfD4)
    pIKdrs = numpy.array(IKdrsD4)
    pIKCa = numpy.array(IKCaD4)
    pIm = numpy.array(ImD4)
    pIl = numpy.array(IlD4)
    pINa = numpy.array(INaD4)
    pICaT = numpy.array(ICaTD4)
    pICaL = numpy.array(ICaLD4)
    pIh = numpy.array(IhD4)
    
    TStart = 10001
    r0 = [pIKa[TStart:],pIKdrf[TStart:],pIKdrs[TStart:],pIKCa[TStart:],pIm[TStart:],pIl[TStart:],pINa[TStart:],pICaT[TStart:],pICaL[TStart:],pIh[TStart:]]
    numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + '_VitroCurrentsD4.npy',r0)
    numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_RandSeed_' + str(y) + '_VitroVoltageD4.npy',vvec0[TStart:])
    TStart = 90001
    r0 = [pIKa[TStart:],pIKdrf[TStart:],pIKdrs[TStart:],pIKCa[TStart:],pIm[TStart:],pIl[TStart:],pINa[TStart:],pICaT[TStart:],pICaL[TStart:],pIh[TStart:]]
    
    fig0 = plotCurrentscape(vvec0[TStart:], r0)
    fig0.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_seed_' + str(y) + '_CurrentscapeInVitro_D4.pdf',dpi=500)
    fig0.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_seed_' + str(y) + '_CurrentscapeInVitro_D4.png',dpi=500)
    fig0.clf()
    plt.close(fig0)
    
    IKa_area0_D4[y] = numpy.trapz(pIKa,t_vec)
    IKdrf_area0_D4[y] = numpy.trapz(pIKdrf,t_vec)
    IKdrs_area0_D4[y] = numpy.trapz(pIKdrs,t_vec)
    IKCa_area0_D4[y] = numpy.trapz(pIKCa,t_vec)
    Im_area0_D4[y] = numpy.trapz(pIm,t_vec)
    Il_area0_D4[y] = numpy.trapz(pIl,t_vec)
    INa_area0_D4[y] = numpy.trapz(pINa,t_vec)
    ICaT_area0_D4[y] = numpy.trapz(pICaT,t_vec)
    ICaL_area0_D4[y] = numpy.trapz(pICaL,t_vec)
    Ih_area0_D4[y] = numpy.trapz(pIh,t_vec)
    
    

numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKa_area0.npy',IKa_area0)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrf_area0.npy',IKdrf_area0)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrs_area0.npy',IKdrs_area0)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKCa_area0.npy',IKCa_area0)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Im_area0.npy',Im_area0)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Il_area0.npy',Il_area0)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_INa_area0.npy',INa_area0)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_ICaT_area0.npy',ICaT_area0)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_ICaL_area0.npy',ICaL_area0)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Ih_area0.npy',Ih_area0)

numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKa_area1.npy',IKa_area1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrf_area1.npy',IKdrf_area1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrs_area1.npy',IKdrs_area1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKCa_area1.npy',IKCa_area1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Im_area1.npy',Im_area1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Il_area1.npy',Il_area1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_INa_area1.npy',INa_area1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_ICaT_area1.npy',ICaT_area1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_ICaL_area1.npy',ICaL_area1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Ih_area1.npy',Ih_area1)

# Dendrite 1
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKa_area0_D1.npy',IKa_area0_D1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrf_area0_D1.npy',IKdrf_area0_D1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrs_area0_D1.npy',IKdrs_area0_D1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKCa_area0_D1.npy',IKCa_area0_D1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Im_area0_D1.npy',Im_area0_D1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Il_area0_D1.npy',Il_area0_D1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_INa_area0_D1.npy',INa_area0_D1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_ICaT_area0_D1.npy',ICaT_area0_D1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_ICaL_area0_D1.npy',ICaL_area0_D1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Ih_area0_D1.npy',Ih_area0_D1)

numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKa_area1_D1.npy',IKa_area1_D1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrf_area1_D1.npy',IKdrf_area1_D1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrs_area1_D1.npy',IKdrs_area1_D1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKCa_area1_D1.npy',IKCa_area1_D1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Im_area1_D1.npy',Im_area1_D1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Il_area1_D1.npy',Il_area1_D1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_INa_area1_D1.npy',INa_area1_D1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_ICaT_area1_D1.npy',ICaT_area1_D1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_ICaL_area1_D1.npy',ICaL_area1_D1)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Ih_area1_D1.npy',Ih_area1_D1)

# Dendrite 2
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKa_area0_D2.npy',IKa_area0_D2)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrf_area0_D2.npy',IKdrf_area0_D2)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrs_area0_D2.npy',IKdrs_area0_D2)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKCa_area0_D2.npy',IKCa_area0_D2)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Im_area0_D2.npy',Im_area0_D2)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Il_area0_D2.npy',Il_area0_D2)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_INa_area0_D2.npy',INa_area0_D2)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_ICaT_area0_D2.npy',ICaT_area0_D2)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_ICaL_area0_D2.npy',ICaL_area0_D2)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Ih_area0_D2.npy',Ih_area0_D2)

numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKa_area1_D2.npy',IKa_area1_D2)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrf_area1_D2.npy',IKdrf_area1_D2)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrs_area1_D2.npy',IKdrs_area1_D2)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKCa_area1_D2.npy',IKCa_area1_D2)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Im_area1_D2.npy',Im_area1_D2)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Il_area1_D2.npy',Il_area1_D2)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_INa_area1_D2.npy',INa_area1_D2)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_ICaT_area1_D2.npy',ICaT_area1_D2)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_ICaL_area1_D2.npy',ICaL_area1_D2)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Ih_area1_D2.npy',Ih_area1_D2)

# Dendrite 3
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKa_area0_D3.npy',IKa_area0_D3)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrf_area0_D3.npy',IKdrf_area0_D3)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrs_area0_D3.npy',IKdrs_area0_D3)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKCa_area0_D3.npy',IKCa_area0_D3)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Im_area0_D3.npy',Im_area0_D3)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Il_area0_D3.npy',Il_area0_D3)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_INa_area0_D3.npy',INa_area0_D3)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_ICaT_area0_D3.npy',ICaT_area0_D3)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_ICaL_area0_D3.npy',ICaL_area0_D3)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Ih_area0_D3.npy',Ih_area0_D3)

numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKa_area1_D3.npy',IKa_area1_D3)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrf_area1_D3.npy',IKdrf_area1_D3)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrs_area1_D3.npy',IKdrs_area1_D3)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKCa_area1_D3.npy',IKCa_area1_D3)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Im_area1_D3.npy',Im_area1_D3)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Il_area1_D3.npy',Il_area1_D3)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_INa_area1_D3.npy',INa_area1_D3)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_ICaT_area1_D3.npy',ICaT_area1_D3)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_ICaL_area1_D3.npy',ICaL_area1_D3)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Ih_area1_D3.npy',Ih_area1_D3)

# Dendrite 4
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKa_area0_D4.npy',IKa_area0_D4)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrf_area0_D4.npy',IKdrf_area0_D4)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrs_area0_D4.npy',IKdrs_area0_D4)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKCa_area0_D4.npy',IKCa_area0_D4)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Im_area0_D4.npy',Im_area0_D4)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Il_area0_D4.npy',Il_area0_D4)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_INa_area0_D4.npy',INa_area0_D4)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_ICaT_area0_D4.npy',ICaT_area0_D4)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_ICaL_area0_D4.npy',ICaL_area0_D4)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Ih_area0_D4.npy',Ih_area0_D4)

numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKa_area1_D4.npy',IKa_area1_D4)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrf_area1_D4.npy',IKdrf_area1_D4)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrs_area1_D4.npy',IKdrs_area1_D4)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_IKCa_area1_D4.npy',IKCa_area1_D4)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Im_area1_D4.npy',Im_area1_D4)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Il_area1_D4.npy',Il_area1_D4)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_INa_area1_D4.npy',INa_area1_D4)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_ICaT_area1_D4.npy',ICaT_area1_D4)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_ICaL_area1_D4.npy',ICaL_area1_D4)
numpy.save('NPYFiles_' + Cell_Name + '/' + Case + '_Ih_area1_D4.npy',Ih_area1_D4)


# IF LOADING INSTEAD
# IKa_area0 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_IKa_area0.npy')
# IKdrf_area0 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrf_area0.npy')
# IKdrs_area0 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrs_area0.npy')
# IKCa_area0 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_IKCa_area0.npy')
# Im_area0 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_Im_area0.npy')
# Il_area0 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_Il_area0.npy')
# INa_area0 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_INa_area0.npy')
# ICaT_area0 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_ICaT_area0.npy')
# ICaL_area0 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_ICaL_area0.npy')
# Ih_area0 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_Ih_area0.npy')
#
# IKa_area1 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_IKa_area1.npy')
# IKdrf_area1 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrf_area1.npy')
# IKdrs_area1 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_IKdrs_area1.npy')
# IKCa_area1 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_IKCa_area1.npy')
# Im_area1 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_Im_area1.npy')
# Il_area1 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_Il_area1.npy')
# INa_area1 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_INa_area1.npy')
# ICaT_area1 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_ICaT_area1.npy')
# ICaL_area1 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_ICaL_area1.npy')
# Ih_area1 = numpy.load('NPYFiles_' + Cell_Name + '/' + Case + '_Ih_area1.npy')


# Plot Current Areas
for y in range(0,5):
    plt.plot(numpy.array([1,2]),numpy.array([IKa_area0[y],IKa_area1[y]]), color = 'tab:blue', label = 'IKa',marker='o', linestyle='solid')
    plt.plot(numpy.array([3,4]),numpy.array([IKa_area0_D1[y],IKa_area1_D1[y]]), color = 'tab:blue', label = 'IKa',marker='o', linestyle='solid')
    plt.plot(numpy.array([5,6]),numpy.array([IKa_area0_D2[y],IKa_area1_D2[y]]), color = 'tab:blue', label = 'IKa',marker='o', linestyle='solid')
    plt.plot(numpy.array([7,8]),numpy.array([IKa_area0_D3[y],IKa_area1_D3[y]]), color = 'tab:blue', label = 'IKa',marker='o', linestyle='solid')
    plt.plot(numpy.array([9,10]),numpy.array([IKa_area0_D4[y],IKa_area1_D4[y]]), color = 'tab:blue', label = 'IKa',marker='o', linestyle='solid')

plt.xlim(0.5,10.5)
plt.xticks(numpy.array([1,2,3,4,5,6,7,8,9,10]),numpy.array(['In Vitro S','In Vivo S','In Vitro D1','In Vivo D1','In Vitro D2','In Vivo D2','In Vitro D3','In Vivo D3','In Vitro D4','In Vivo D4',]),rotation = 45)
plt.ylabel('Current Area (' + r'$nA \times ms)$')
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_IKa.pdf', bbox_inches='tight')
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_IKa.png', bbox_inches='tight')
plt.gcf().clear()
plt.cla()
plt.clf()
plt.close()

for y in range(0,5):
    plt.plot(numpy.array([1,2]),numpy.array([IKdrf_area0[y],IKdrf_area1[y]]), color = 'tab:orange', label = 'IKdrf',marker='o', linestyle='solid')
    plt.plot(numpy.array([3,4]),numpy.array([IKdrf_area0_D1[y],IKdrf_area1_D1[y]]), color = 'tab:orange', label = 'IKdrf',marker='o', linestyle='solid')
    plt.plot(numpy.array([5,6]),numpy.array([IKdrf_area0_D2[y],IKdrf_area1_D2[y]]), color = 'tab:orange', label = 'IKdrf',marker='o', linestyle='solid')
    plt.plot(numpy.array([7,8]),numpy.array([IKdrf_area0_D3[y],IKdrf_area1_D3[y]]), color = 'tab:orange', label = 'IKdrf',marker='o', linestyle='solid')
    plt.plot(numpy.array([9,10]),numpy.array([IKdrf_area0_D4[y],IKdrf_area1_D4[y]]), color = 'tab:orange', label = 'IKdrf',marker='o', linestyle='solid')

plt.xlim(0.5,10.5)
plt.xticks(numpy.array([1,2,3,4,5,6,7,8,9,10]),numpy.array(['In Vitro S','In Vivo S','In Vitro D1','In Vivo D1','In Vitro D2','In Vivo D2','In Vitro D3','In Vivo D3','In Vitro D4','In Vivo D4',]),rotation = 45)
plt.ylabel('Current Area (' + r'$nA \times ms)$')
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_IKdrf.pdf', bbox_inches='tight')
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_IKdrf.png', bbox_inches='tight')
plt.gcf().clear()
plt.cla()
plt.clf()
plt.close()

for y in range(0,5):
    plt.plot(numpy.array([1,2]),numpy.array([IKdrs_area0[y],IKdrs_area1[y]]), color = 'tab:green', label = 'IKdrs',marker='o', linestyle='solid')
    plt.plot(numpy.array([3,4]),numpy.array([IKdrs_area0_D1[y],IKdrs_area1_D1[y]]), color = 'tab:green', label = 'IKdrs',marker='o', linestyle='solid')
    plt.plot(numpy.array([5,6]),numpy.array([IKdrs_area0_D2[y],IKdrs_area1_D2[y]]), color = 'tab:green', label = 'IKdrs',marker='o', linestyle='solid')
    plt.plot(numpy.array([7,8]),numpy.array([IKdrs_area0_D3[y],IKdrs_area1_D3[y]]), color = 'tab:green', label = 'IKdrs',marker='o', linestyle='solid')
    plt.plot(numpy.array([9,10]),numpy.array([IKdrs_area0_D4[y],IKdrs_area1_D4[y]]), color = 'tab:green', label = 'IKdrs',marker='o', linestyle='solid')

plt.xlim(0.5,10.5)
plt.xticks(numpy.array([1,2,3,4,5,6,7,8,9,10]),numpy.array(['In Vitro S','In Vivo S','In Vitro D1','In Vivo D1','In Vitro D2','In Vivo D2','In Vitro D3','In Vivo D3','In Vitro D4','In Vivo D4',]),rotation = 45)
plt.ylabel('Current Area (' + r'$nA \times ms)$')
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_IKdrs.pdf', bbox_inches='tight')
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_IKdrs.png', bbox_inches='tight')
plt.gcf().clear()
plt.cla()
plt.clf()
plt.close()

for y in range(0,5):
    plt.plot(numpy.array([1,2]),numpy.array([IKCa_area0[y],IKCa_area1[y]]), color = 'tab:red', label = 'IKCa',marker='o', linestyle='solid')
    plt.plot(numpy.array([3,4]),numpy.array([IKCa_area0_D1[y],IKCa_area1_D1[y]]), color = 'tab:red', label = 'IKCa',marker='o', linestyle='solid')
    plt.plot(numpy.array([5,6]),numpy.array([IKCa_area0_D2[y],IKCa_area1_D2[y]]), color = 'tab:red', label = 'IKCa',marker='o', linestyle='solid')
    plt.plot(numpy.array([7,8]),numpy.array([IKCa_area0_D3[y],IKCa_area1_D3[y]]), color = 'tab:red', label = 'IKCa',marker='o', linestyle='solid')
    plt.plot(numpy.array([9,10]),numpy.array([IKCa_area0_D4[y],IKCa_area1_D4[y]]), color = 'tab:red', label = 'IKCa',marker='o', linestyle='solid')

plt.xlim(0.5,10.5)
plt.xticks(numpy.array([1,2,3,4,5,6,7,8,9,10]),numpy.array(['In Vitro S','In Vivo S','In Vitro D1','In Vivo D1','In Vitro D2','In Vivo D2','In Vitro D3','In Vivo D3','In Vitro D4','In Vivo D4',]),rotation = 45)
plt.ylabel('Current Area (' + r'$nA \times ms)$')
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_IKCa.pdf', bbox_inches='tight')
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_IKCa.png', bbox_inches='tight')
plt.gcf().clear()
plt.cla()
plt.clf()
plt.close()

for y in range(0,5):
    plt.plot(numpy.array([1,2]),numpy.array([Im_area0[y],Im_area1[y]]), color = 'tab:purple', label = 'Im',marker='o', linestyle='solid')
    plt.plot(numpy.array([3,4]),numpy.array([Im_area0_D1[y],Im_area1_D1[y]]), color = 'tab:purple', label = 'Im',marker='o', linestyle='solid')
    plt.plot(numpy.array([5,6]),numpy.array([Im_area0_D2[y],Im_area1_D2[y]]), color = 'tab:purple', label = 'Im',marker='o', linestyle='solid')
    plt.plot(numpy.array([7,8]),numpy.array([Im_area0_D3[y],Im_area1_D3[y]]), color = 'tab:purple', label = 'Im',marker='o', linestyle='solid')
    plt.plot(numpy.array([9,10]),numpy.array([Im_area0_D4[y],Im_area1_D4[y]]), color = 'tab:purple', label = 'Im',marker='o', linestyle='solid')

plt.xlim(0.5,10.5)
plt.xticks(numpy.array([1,2,3,4,5,6,7,8,9,10]),numpy.array(['In Vitro S','In Vivo S','In Vitro D1','In Vivo D1','In Vitro D2','In Vivo D2','In Vitro D3','In Vivo D3','In Vitro D4','In Vivo D4',]),rotation = 45)
plt.ylabel('Current Area (' + r'$nA \times ms)$')
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_Im.pdf', bbox_inches='tight')
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_Im.png', bbox_inches='tight')
plt.gcf().clear()
plt.cla()
plt.clf()
plt.close()

for y in range(0,5):
    plt.plot(numpy.array([1,2]),numpy.array([Il_area0[y],Il_area1[y]]), color = 'tab:brown', label = 'Il',marker='o', linestyle='solid')
    plt.plot(numpy.array([3,4]),numpy.array([Il_area0_D1[y],Il_area1_D1[y]]), color = 'tab:brown', label = 'Il',marker='o', linestyle='solid')
    plt.plot(numpy.array([5,6]),numpy.array([Il_area0_D2[y],Il_area1_D2[y]]), color = 'tab:brown', label = 'Il',marker='o', linestyle='solid')
    plt.plot(numpy.array([7,8]),numpy.array([Il_area0_D3[y],Il_area1_D3[y]]), color = 'tab:brown', label = 'Il',marker='o', linestyle='solid')
    plt.plot(numpy.array([9,10]),numpy.array([Il_area0_D4[y],Il_area1_D4[y]]), color = 'tab:brown', label = 'Il',marker='o', linestyle='solid')

plt.xlim(0.5,10.5)
plt.xticks(numpy.array([1,2,3,4,5,6,7,8,9,10]),numpy.array(['In Vitro S','In Vivo S','In Vitro D1','In Vivo D1','In Vitro D2','In Vivo D2','In Vitro D3','In Vivo D3','In Vitro D4','In Vivo D4',]),rotation = 45)
plt.ylabel('Current Area (' + r'$nA \times ms)$')
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_Il.pdf', bbox_inches='tight')
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_Il.png', bbox_inches='tight')
plt.gcf().clear()
plt.cla()
plt.clf()
plt.close()

for y in range(0,5):
    plt.plot(numpy.array([1,2]),numpy.array([INa_area0[y],INa_area1[y]]), color = 'tab:pink', label = 'INa',marker='o', linestyle='solid')
    plt.plot(numpy.array([3,4]),numpy.array([INa_area0_D1[y],INa_area1_D1[y]]), color = 'tab:pink', label = 'INa',marker='o', linestyle='solid')
    plt.plot(numpy.array([5,6]),numpy.array([INa_area0_D2[y],INa_area1_D2[y]]), color = 'tab:pink', label = 'INa',marker='o', linestyle='solid')
    plt.plot(numpy.array([7,8]),numpy.array([INa_area0_D3[y],INa_area1_D3[y]]), color = 'tab:pink', label = 'INa',marker='o', linestyle='solid')
    plt.plot(numpy.array([9,10]),numpy.array([INa_area0_D4[y],INa_area1_D4[y]]), color = 'tab:pink', label = 'INa',marker='o', linestyle='solid')

plt.xlim(0.5,10.5)
plt.xticks(numpy.array([1,2,3,4,5,6,7,8,9,10]),numpy.array(['In Vitro S','In Vivo S','In Vitro D1','In Vivo D1','In Vitro D2','In Vivo D2','In Vitro D3','In Vivo D3','In Vitro D4','In Vivo D4',]),rotation = 45)
plt.ylabel('Current Area (' + r'$nA \times ms)$')
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_INa.pdf', bbox_inches='tight')
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_INa.png', bbox_inches='tight')
plt.gcf().clear()
plt.cla()
plt.clf()
plt.close()

for y in range(0,5):
    plt.plot(numpy.array([1,2]),numpy.array([ICaT_area0[y],ICaT_area1[y]]), color = 'tab:gray', label = 'ICaT',marker='o', linestyle='solid')
    plt.plot(numpy.array([3,4]),numpy.array([ICaT_area0_D1[y],ICaT_area1_D1[y]]), color = 'tab:gray', label = 'ICaT',marker='o', linestyle='solid')
    plt.plot(numpy.array([5,6]),numpy.array([ICaT_area0_D2[y],ICaT_area1_D2[y]]), color = 'tab:gray', label = 'ICaT',marker='o', linestyle='solid')
    plt.plot(numpy.array([7,8]),numpy.array([ICaT_area0_D3[y],ICaT_area1_D3[y]]), color = 'tab:gray', label = 'ICaT',marker='o', linestyle='solid')
    plt.plot(numpy.array([9,10]),numpy.array([ICaT_area0_D4[y],ICaT_area1_D4[y]]), color = 'tab:gray', label = 'ICaT',marker='o', linestyle='solid')

plt.xlim(0.5,10.5)
plt.xticks(numpy.array([1,2,3,4,5,6,7,8,9,10]),numpy.array(['In Vitro S','In Vivo S','In Vitro D1','In Vivo D1','In Vitro D2','In Vivo D2','In Vitro D3','In Vivo D3','In Vitro D4','In Vivo D4',]),rotation = 45)
plt.ylabel('Current Area (' + r'$nA \times ms)$')
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_ICaT.pdf', bbox_inches='tight')
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_ICaT.png', bbox_inches='tight')
plt.gcf().clear()
plt.cla()
plt.clf()
plt.close()

for y in range(0,5):
    plt.plot(numpy.array([1,2]),numpy.array([ICaL_area0[y],ICaL_area1[y]]), color = 'tab:olive', label = 'ICaL',marker='o', linestyle='solid')
    plt.plot(numpy.array([3,4]),numpy.array([ICaL_area0_D1[y],ICaL_area1_D1[y]]), color = 'tab:olive', label = 'ICaL',marker='o', linestyle='solid')
    plt.plot(numpy.array([5,6]),numpy.array([ICaL_area0_D2[y],ICaL_area1_D2[y]]), color = 'tab:olive', label = 'ICaL',marker='o', linestyle='solid')
    plt.plot(numpy.array([7,8]),numpy.array([ICaL_area0_D3[y],ICaL_area1_D3[y]]), color = 'tab:olive', label = 'ICaL',marker='o', linestyle='solid')
    plt.plot(numpy.array([9,10]),numpy.array([ICaL_area0_D4[y],ICaL_area1_D4[y]]), color = 'tab:olive', label = 'ICaL',marker='o', linestyle='solid')

plt.xlim(0.5,10.5)
plt.xticks(numpy.array([1,2,3,4,5,6,7,8,9,10]),numpy.array(['In Vitro S','In Vivo S','In Vitro D1','In Vivo D1','In Vitro D2','In Vivo D2','In Vitro D3','In Vivo D3','In Vitro D4','In Vivo D4',]),rotation = 45)
plt.ylabel('Current Area (' + r'$nA \times ms)$')
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_ICaL.pdf', bbox_inches='tight')
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_ICaL.png', bbox_inches='tight')
plt.gcf().clear()
plt.cla()
plt.clf()
plt.close()

for y in range(0,5):
    plt.plot(numpy.array([1,2]),numpy.array([Ih_area0[y],Ih_area1[y]]), color = 'tab:cyan', label = 'Ih',marker='o', linestyle='solid')
    plt.plot(numpy.array([3,4]),numpy.array([Ih_area0_D1[y],Ih_area1_D1[y]]), color = 'tab:cyan', label = 'Ih',marker='o', linestyle='solid')
    plt.plot(numpy.array([5,6]),numpy.array([Ih_area0_D2[y],Ih_area1_D2[y]]), color = 'tab:cyan', label = 'Ih',marker='o', linestyle='solid')
    plt.plot(numpy.array([7,8]),numpy.array([Ih_area0_D3[y],Ih_area1_D3[y]]), color = 'tab:cyan', label = 'Ih',marker='o', linestyle='solid')
    plt.plot(numpy.array([9,10]),numpy.array([Ih_area0_D4[y],Ih_area1_D4[y]]), color = 'tab:cyan', label = 'Ih',marker='o', linestyle='solid')

plt.xlim(0.5,10.5)
plt.xticks(numpy.array([1,2,3,4,5,6,7,8,9,10]),numpy.array(['In Vitro S','In Vivo S','In Vitro D1','In Vivo D1','In Vitro D2','In Vivo D2','In Vitro D3','In Vivo D3','In Vitro D4','In Vivo D4',]),rotation = 45)
plt.ylabel('Current Area (' + r'$nA \times ms)$')
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_Ih.pdf', bbox_inches='tight')
plt.savefig('Plots_' + Cell_Name + '/' + Cell_Name + '_Ih.png', bbox_inches='tight')
plt.gcf().clear()
plt.cla()
plt.clf()
plt.close()


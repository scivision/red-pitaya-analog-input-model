#!/usr/bin/env python
from pathlib import Path
from numpy import loadtxt,log10
from matplotlib.pyplot import figure,show
import seaborn
seaborn.set_style('whitegrid')

lfn = Path('LV.out')
hfn = Path('HV.out')

ldat = loadtxt(lfn)
hdat = loadtxt(hfn)
   
f = ldat[:,0]
#%%
ax = figure().gca()

ax.plot(f, 20*log10(ldat[:,2]/ldat[:,1]),label='LV')
ax.plot(f, 20*log10(hdat[:,2]/hdat[:,1]),label='HV')
ax.plot(f, 20*log10(hdat[:,2]/ldat[:,2]),label='HV/LV')


ax.set_xlabel('frequency [Hz]')
ax.set_ylabel('gain [dB]')
ax.set_title('Transfer Function $H(f)$')
ax.autoscale(True,axis='x',tight=True)
ax.set_xscale('log')

ax.legend()

show()
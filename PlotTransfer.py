#!/usr/bin/env python
from pathlib import Path
from numpy import loadtxt,log10
from matplotlib.pyplot import figure,show
import seaborn
seaborn.set_style('whitegrid')

fn = Path('LV.out')


dat = loadtxt(fn)

T = dat[:,2]/dat[:,1]
#%%
ax = figure().gca()
ax.plot(dat[:,0], 20*log10(T))
ax.set_xlabel('frequency [Hz]')
ax.set_ylabel('gain [dB]')
ax.set_title(f'{fn.stem} Transfer Function $H(f)$')
ax.autoscale(True,axis='x',tight=True)
ax.set_xscale('log')
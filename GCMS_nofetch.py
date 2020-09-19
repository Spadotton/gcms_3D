#!/usr/bin/env python2
import csv
import numpy as np
import matplotlib.pyplot as plt
from Tkinter import *

filename1="isooctane_nist.csv"
filename2="isooctane1_exp.csv"

data1 = np.loadtxt(filename1, delimiter=",")
data2 = np.loadtxt(filename2, delimiter=",")

mass1 = data1[:,0]
rint1 = data1[:,1]
yint1 = (rint1/max(rint1))*100

mass2 = data2[:,0]
rint2 = data2[:,1]
yint2 = (rint2/max(rint2))*100

x1 = []
y2 = [0]
x1 = []
x2 = [0]
 
with open("out.csv","w") as f:
    cr = csv.writer(f,delimiter=";",lineterminator="\n")
    cr.writerow(["a","b","c"])
    cr.writerow(["d","e","f"])
    cr.writerow(["a","b","c"])
    cr.writerow(["d","e","f"])

x1,y1 = (mass1, yint1)
x2,y2 = (mass2, yint2)

fig, ax= plt.subplots()
ax.plot(x1,y1, 'r-')
ax.acorr(x1, usevlines=True, normed=True, maxlags=35, lw=2)
ax.set_xlabel('m/z')
ax.grid(True)
ax.set_xlim(0, 150)
ax.set_ylabel('relative intensity')
ax.set_title('NIST vs SMPL \n isooctane')

ax.plot(x2,y2, 'b--')
ax.acorr(x2, usevlines=True, normed=True, maxlags=50, lw=2)
ax.grid(True)
ax.set_xlim(0, 150)
ax.axhline(0, color='black', lw=2)

fig.tight_layout()
plt.show()


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a python script to plot an Appleman Diagram
after downloading an atmospheric radiosounding 
(e.g. http://weather.uwyo.edu/upperair/sounding.html )
Here we show an exaple for the city of Florianópolis-SC, Brazil
It´s in support to the article by 
Lins V and Ramos-da-Silva R, Physical processes analysis of contrails formation over the South Brazil Region,
Revista Ciência e Natura, 2020.
"""
import numpy as np
import matplotlib.pyplot as plt

#Read the uploaded radiosonde data
P=np.loadtxt("radio-fln-08set2017-12Z.txt")[:, 0]
H=np.loadtxt("radio-fln-08set2017-12Z.txt")[:, 1]
T=np.loadtxt("radio-fln-08set2017-12Z.txt")[:, 2]
Td=np.loadtxt("radio-fln-08set2017-12Z.txt")[:, 3]
UR=np.loadtxt("radio-fln-08set2017-12Z.txt")[:, 4]
mix=np.loadtxt("radio-fln-08set2017-12Z.txt")[:, 5]
DIR=np.loadtxt("radio-fln-08set2017-12Z.txt")[:, 6]
SPEED=np.loadtxt("radio-fln-08set2017-12Z.txt")[:, 7]
Theta=np.loadtxt("radio-fln-08set2017-12Z.txt")[:, 8]
Thetae=np.loadtxt("radio-fln-08set2017-12Z.txt")[:, 9]
Thetav=np.loadtxt("radio-fln-08set2017-12Z.txt")[:, 10]

#Diagrama Appleman
pr=[1000, 900, 800, 700, 600, 500, 450, 400, 350, 300, 250, 200, 175, 150, 130, 115, 100] 
trh0=[-37.15, -38.30, -39.58, -41.00, -42.62, -44.50, -45.57, -46.75, -48.07, -49.58, -51.33,-53.43, -54.67, -56.07, -57.36, -58.45, -59.68]
trh30 = [-35.84, -37.00, -38.29, -39.73, -41.37, -43.27, -44.36, -45.55, -46.89, -48.42,-50.19, -52.31, -53.56, -54.99, -56.29, -57.39, -58.63] 
tr100 = [-26.15, -27.43, -28.84, -30.40, -32.18, -34.28, -35.46, -36.77, -38.23, -39.87,-41.80, -44.12, -45.42, -47.01, -48.43, -49.61, -50.92]
tmax=[-32.42, -33.73, -35.17, -36.77, -38.58, -40.67,-41.85, -43.16, -44.61,-46.25,-48.16, -50.44,-51.77, -53.28,-54.66, -55.82, -57.13]

plt.plot(trh0, pr, 'b-')
plt.plot(trh30, pr, 'b-.')
plt.plot(tr100, pr, 'b--')
plt.plot(tmax,pr,'m-*')

# Sounding data
plt.plot(T,P,'r-o')

plt.gca().invert_yaxis()
plt.ylim((500,100))
plt.xlim((-70,-10))

plt.legend(['Trh0', 'Tr30', 'Tr100', 'Persistence', 'OBS-FLN'])
plt.grid(True)

plt.text(-70, 210, 'Always', fontsize=12)
plt.text(-70, 240, 'Contrails', fontsize=12)
plt.text(-53, 150, 'May', fontsize=12)
plt.text(-51, 180, 'Be', fontsize=12)
plt.text(-43, 180, 'No Contrails', fontsize=12)

# Add title and legend
plt.title('Florianopolis 08/Sep/2017 12Z')
plt.xlabel('Temp(C)')
plt.ylabel('Press (hPa)')

# Save the figure
plt.savefig('f08set2017.tiff', dpi=600, format="tiff")


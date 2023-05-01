import harmonic_oscillator as ho
import numpy as np
import matplotlib.pyplot as plt

vrijeme_trajectory=[0.001,0.01,0.1,1]
vrijeme_period=[0.01,0.1,0.2,0.3]
p1=ho.HarmonicOscillator(2,2,10,0)
for i in vrijeme_trajectory:
    p1.plot_trajectory(0,10,i)
for i in vrijeme_period: #Ne mora nužno konvergirat period s jedne strane svakim korakom prema analitičkom periodu jer postoji greška u razmaku između mijenjanja 2 predznaka
    p1.graf_period(i)
plt.xlabel('T[s]')
plt.ylabel('A[m]')
plt.title('Period harmonijskog titranja')
plt.legend()
plt.show()
from particle import Particle
import numpy as np

p2=Particle(10,45,(10,10))
p2.plot_trajectory()
#Analitičko rješavanje
v0=10
g=10
kut=(45/180)*np.pi
t=2*v0*np.sin(kut)/g
D1=v0*np.cos(kut)*t
print(D1)
#Numeričko rješavanje
D2=p2.range()
print(D2)
#Numeričko i analitičko rješenje nije isto

#Pogreška
if D1-D2>=0:
    Pogreška=((D1-D2)/D1)*100
else:
    Pogreška=((D2-D1)/D1)*100
print('Pogreška iznosi {} %.'.format(Pogreška))
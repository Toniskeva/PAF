import projectile as projectile
import numpy as np
import matplotlib.pyplot as plt

p1=projectile.Projectile(200,45,0,0,1,0.1)

vrijeme=[0.001,0.01,0.1,0.5,1]
for i in vrijeme:
    p1.plot_trajectory(i,1.25,0.1)
plt.title('y-x graf')
plt.xlabel('x[m]')
plt.ylabel('y[m]')
plt.legend()
plt.show()

p1.plot_trajectory(0.01,1.25,0.1)
p1.plot_trajectory(0.001,1.25,0.1)
p1.runge_kutta_plot_trajectory(0.01,1.25,0.1)
plt.xlabel('x[m]')
plt.ylabel('y[m]')
plt.title('y-x graf')
plt.legend()
plt.show()
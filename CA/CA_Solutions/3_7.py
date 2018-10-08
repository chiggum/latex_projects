import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.animation as animation
np.random.seed(2)
##
n = 10000
x = np.random.uniform(-1., 1., n)
binry = np.random.randint(0, 2, n)
y = np.sqrt(1 - x*x) * (2 * binry - 1)
##
r_s = 0.1
r_e = 10
##
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
fig = plt.figure()
pltlist = []
while r_s < r_e:
    xx = r_s * x
    yy = r_s * y
    plt.plot([0],[0],"r,")
    e_x = np.exp(xx)*np.cos(yy)
    e_y = np.exp(xx)*np.sin(yy)
    myplt = plt.plot(e_x,e_y,"b,")
    pltlist.append(myplt)
    plt.show()
    r_s += 0.1

ani = animation.ArtistAnimation(fig, pltlist, interval=50, blit=True, repeat_delay=1000)
#ani.save('4_1_2.mp4', writer=writer)
plt.show()
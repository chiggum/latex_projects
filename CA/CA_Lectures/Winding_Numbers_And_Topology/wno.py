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
a_x = 1
a_y = 1
b_x = 1
b_y = 1
c_x = 3
c_y = 3
##
r_s = 0.1
r_e = 7
##
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
fig = plt.figure()
pltlist = []
while r_s < r_e:
    xx = r_s * x
    yy = r_s * y
    plt.plot([0],[0],"r,")
    d_x = (xx-a_x)*(xx-b_x) - (yy-a_y)*(yy-b_y)
    d_y = (xx-a_x)*(yy-b_y) + (yy-a_y)*(xx-b_x)
    e_x = (xx-c_x)*d_x - (yy-c_y)*d_y
    e_y = (xx-c_x)*d_y + (yy-c_y)*d_x
    myplt = plt.plot(e_x,e_y,"b,")
    pltlist.append(myplt)
    r_s += 0.1

ani = animation.ArtistAnimation(fig, pltlist, interval=50, blit=True, repeat_delay=1000)
#ani.save('4_1_2.mp4', writer=writer)
plt.show()
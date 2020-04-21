import numpy as np
import matplotlib.pyplot as plt

L = 100
Brightness = 100
noise_strength = 1

#=============================#

def stack(N):
    D = np.ones((L,L))*Brightness
    for i in range(N):
        noise = np.random.normal(loc=0,size=(L,L),scale=noise_strength)
        D += noise/N
    print("Number of stack:", N)
    print("mean:", np.mean(D))
    print("std:", np.std(D))
    return D

#=============================#

maxv = 110
minv = 90

#=============================#
plt.figure()
fig = plt.subplot(1,3,1)
plt.imshow(stack(#TODO),cmap = 'gray', vmax = maxv, vmin = minv)

fig = plt.subplot(1,3,2)
plt.imshow(stack(#TODO),cmap = 'gray', vmax = maxv, vmin = minv)

fig = plt.subplot(1,3,3)
plt.imshow(stack(#TODO),cmap = 'gray', vmax = maxv, vmin = minv)

plt.show()

import numpy as np
import matplotlib.pyplot as plt

L = 100
Brightness = 100
noise_strength = 1

image = np.ones((L,L))*100
noise = (np.random.random((L,L))-np.ones((L,L))*0.5)*2*noise_strength
image += noise

print("mean:", #TODO)
print("std:", #TODO)

plt.imshow(image,cmap = 'gray')
plt.colorbar()
plt.show()

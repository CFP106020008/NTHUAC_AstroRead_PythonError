import numpy as np
import matplotlib.pyplot as plt

L = 100
Brightness = 100
noise_strength = 1

#=============================#

#Image 1 
image1 = np.ones((L,L))*100
noise = (np.random.random((L,L))-np.ones((L,L))*0.5)*2*noise_strength
image1 += noise
print("mean:", np.mean(image1))
print("std:", np.std(image1))

#=============================#

#Image 2
image2 = 
#TODO

#=============================#

#Combine Image
image_combine = 
print("mean:", np.mean(image_combine))
print("std:", np.std(image_combine))


plt.figure()
fig = plt.subplot(1,3,1)
plt.imshow(image1,cmap = 'gray')

fig = plt.subplot(1,3,2)
plt.imshow(image2,cmap = 'gray')

fig = plt.subplot(1,3,3)
plt.imshow(image_combine,cmap = 'gray')

plt.show()


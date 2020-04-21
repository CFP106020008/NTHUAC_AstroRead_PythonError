import numpy as np
import matplotlib.pyplot as plt

L = 100
D = np.zeros((L,L)) #The image we draw on

#=========================#

T = 100 #Exposure time

#=========================#

#Star
#Star is usually a gaussian profile
S = 100
Star = np.zeros((L,L))
sigma = 5.0 #The width of FWHM
mu = np.array([50,50]) #The center of the star
for i in range(L):
    for j in range(L):
        Star[i,j] = S*np.exp(-((i-mu[0])**2+(j-mu[1])**2)/(2.0*sigma**2))*T

#Noise is poisson noise => N ~ S**0.5
Source_noise = np.random.normal(size = (L,L), loc = 0, scale = Star**0.5)

#=========================#

#Dark
#Dark current is the electron kicked out by the thermal random motion
Dark_strength = 100
Dark = np.ones((L,L))*Dark_strength*T
Dark_noise = np.random.normal(loc = 0, size = (L,L), scale = Dark**0.5)

#=========================#

#Bias
Bias_strength = 100
Bias = np.ones((L,L))*Bias_strength

#=========================#

#Light pollution
#Let's first assume a uniform sky background
LightPollutionStrength = 100
LightPollution = np.ones((L,L))*LightPollutionStrength
LP_noise = np.random.normal(loc = 0, size = (L,L), scale = LightPollution**0.5)

#=========================#

#Add all the source and noise
D += Star
D += Source_noise
#D += Dark
D += Dark_noise
#D += Bias
#D += LightPollution
D += LP_noise

#=========================#

#Showing the final image
plt.imshow(D)
plt.colorbar()
plt.show()

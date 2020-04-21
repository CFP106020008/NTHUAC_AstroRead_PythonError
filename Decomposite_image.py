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
sigma =  #The width of FWHM
mu = np.array([50,50]) #The center of the star
for i in range(L):
    for j in range(L):
        #TODO

#Noise is poisson noise => N ~ S**0.5
Source_noise = #TODO

#=========================#

#Dark
#Dark current is the electron kicked out by the thermal random motion
Dark_strength = 100
Dark = #TODO
Dark_noise = #TODO

#=========================#

#Bias
Bias_strength = 100
Bias = #TODO

#=========================#

#Light pollution
#Let's first assume a uniform sky background
LightPollutionStrength = 100
LightPollution = #TODO
LP_noise = #TODO

#=========================#

#Add all the source and noise
D += Star
D += Source_noise
D += Dark
D += Dark_noise
D += Bias
D += LightPollution
D += LP_noise

#=========================#

#Showing the final image
plt.imshow(D)
plt.colorbar()
plt.show()

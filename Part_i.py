from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np


observation_seq = [1, 0, 0, 1, 0, 0, 0, 1]
vh, vt = 1, 1
# Calculation of beta prior with beta(1,1).
x = np.linspace(beta.ppf(0.01, vh, vt), beta.ppf(0.99, vh, vt), 100)
plt.subplot(3, 3, 1)
plt.xlabel('Hypothesis')
plt.ylabel('Beta prior probability')
plt.plot(x, beta.pdf(x, vh, vt), 'r-', label='beta(1,1)')
plt.legend()
counter = 1

# Calculation of beta posterior for given observation sequence.
h, t = 0, 0
for idx, obs in enumerate(observation_seq):
    counter += 1
    h = h + obs
    t = t + (1-obs)
    x = np.linspace(beta.ppf(0, vh+h, vt+t), beta.ppf(1, vh+h, vt+t), 100)
    k = 'Heads' if obs == 1 else 'Tails'
    plt.subplot(3, 3, counter)
    plt.xlabel('Hypothesis')
    plt.ylabel('Beta posterior probability')
    plt.plot(x, beta.pdf(x, vh+h, vt+t), 'r-', label='trial %d' %(idx+1) + ': h=%d' %h +' t=%d'%t)
    plt.legend()
plt.show()

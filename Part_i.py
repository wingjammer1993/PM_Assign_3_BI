from scipy.stats import beta
import matplotlib.pyplot as plt
import numpy as np


observation_seq = [1, 0, 0, 1, 0, 0, 0, 1]
vh, vt = 1, 1
x = np.linspace(beta.ppf(0.01, vh, vt), beta.ppf(0.99, vh, vt), 100)
plt.xlabel('Hypothesis')
plt.ylabel('Beta prior probability')
plt.title('Prior with Beta({},{})'.format(vh, vt))
plt.plot(x, beta.pdf(x, vh, vt), 'r-', label='beta prior')
plt.show()

h, t = 0, 0
for idx, obs in enumerate(observation_seq):
    h = h + obs
    t = t + (1-obs)
    x = np.linspace(beta.ppf(0, vh+h, vt+t), beta.ppf(1, vh+h, vt+t), 100)
    k = 'Heads' if obs == 1 else 'Tails'
    plt.xlabel('Hypothesis')
    plt.ylabel('Beta posterior probability')
    plt.title('Trial {}: {} with Beta({}, {})'.format(idx, k, vh+h, vt+t))
    plt.plot(x, beta.pdf(x, vh+h, vt+t), 'r-', label='beta prior')
    plt.show()

import math

import matplotlib.pyplot as plt

SQRT_TWO_PI = math.sqrt((math.pi) * 2)

def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:          # here PDF refers to Probability Density Function.
    
    return (math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI / sigma))



xs = [x / 10 for x in range(-50, 50)]


plt.plot(xs,[normal_pdf(x, sigma = 1) for x in xs],'-', label = 'mu = 0, sigma = 1')

plt.plot(xs,[normal_pdf(x, sigma = 2) for x in xs],'--', label = 'mu = 0, sigma = 2')

plt.plot(xs,[normal_pdf(x, sigma = .5) for x in xs],':', label = 'mu = 0, sigma = .5')

plt.plot(xs,[normal_pdf(x, mu = -1) for x in xs],':,', label = 'mu = -1, sigma = 1')

plt.plot(xs,[normal_pdf(x, mu = 3) for x in xs],'*', label = 'mu = 3, sigma = 1')


plt.legend()

plt.title("Various Normal PDF")

plt.show()
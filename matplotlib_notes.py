
import matplotlib.pyplot as plt
import numpy as np

# generate sequence plot
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

# list is converted to numpy array internally
# plot x vs y
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([1, 6, 0, 20])
plt.show()

# multiple lines in one plot
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

# controlling line properties
# use keywords
x = np.arange(0, 6, 0.1) 
y = np.sin(x) + np.random.random(60)
plt.plot(x, y, linewidth=2.0)
line, = plt.plot(x, y, '-')






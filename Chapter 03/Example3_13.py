import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)
y = x**2
plt.figure()
plt.plot(x,y, color = '#4a8c66')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Square of X')
plt.grid()
plt.axis([0,5,0,25])
plt.show()

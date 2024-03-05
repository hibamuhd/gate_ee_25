import numpy as np
import matplotlib.pyplot as plt

# Define the range of x and y values
x = np.linspace(0, 10, 100)  # Range of x values from -10 to 10
y = np.linspace(0, 10, 100)  # Range of y values from -10 to 10

# Plot the graph
plt.plot(x, y, label='y=x for x>0 and y>0', color='blue', linestyle='-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('x=y for x>0 and y>0')
plt.grid(False)

# Add horizontal and vertical lines at y=0 and x=0
plt.axhline(0, color='black', linestyle='-')
plt.axvline(0, color='black', linestyle='-')

# Set the limits of the x and y axes
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.xlim(-10, 10)
plt.ylim(-10, 10)

x_mid = (x[0] + x[-1]) / 2
y_mid = (y[0] + y[-1]) / 2

plt.axhline(0, color='blue', linestyle='-', xmin=-0.5, xmax=-1, linewidth=2, label='y=0 for x<0')
# Add the equation Vo=Vin at the middle point of the line y=x
plt.text(x_mid, y_mid, 'Vo=Vin', fontsize=12, ha='center', va='center')
plt.text(-5, 0.5, 'Vo=0', fontsize=12, ha='center', va='center')

plt.legend()
plt.savefig('gate_25_fig6.png')
plt.show()

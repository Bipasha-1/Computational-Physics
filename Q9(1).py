#9(1).
import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def fun(x, y):
    y1, y2 = y
    dydx = [y2, -np.exp(-2*y1)]
    return dydx

def bc(ya, yb):
    return [ya[0], yb[0] - np.log(2)]

# Interval for x
x = np.linspace(1, 2, 100)

# Initial guess for y1 and y2
y_guess = np.zeros((2, x.size))

# Solve the BVP
sol = solve_bvp(fun, bc, x, y_guess)

# Interpolating the solution to get more points for plotting
x_plot = np.linspace(1, 2, 100)
y_plot = sol.sol(x_plot)[0]

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x_plot, y_plot, label='Numerical solution')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of y" = -e^{-2y}')

plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()

# 9(3)
import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def fun(x, y):
    y1, y2 = y
    dydx = [y2, -(2*y2**3 + y1**2*y2) * 1/np.cos(x)]
    return dydx

def bc(ya, yb):
    return [ya[0] - 2**(-1/4), yb[0] - 0.5*(12)**0.25]

# Interval for x
x = np.linspace(np.pi/4, np.pi/3, 100)

# Initial guess for y1 and y2
y_guess = np.zeros((2, x.size))
y_guess[0] = np.linspace(2**(-1/4), 121/(4*2), x.size)

# Solve the BVP
sol = solve_bvp(fun, bc, x, y_guess)

# Interpolating the solution to get more points for plotting
x_plot = np.linspace(np.pi/4, np.pi/3, 100)
y_plot = sol.sol(x_plot)[0]

# Plotting
plt.figure(figsize=(5, 4))
plt.plot(x_plot, y_plot, label='Numerical solution')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of y" = -(2(y\')^3 + y^2 y\') sec(x)')

plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()

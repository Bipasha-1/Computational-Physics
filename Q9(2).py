import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt
# 9(2)
def ode_system(x, y):
    z = y[1]  # y' = z
    dzdx = z * np.cos(x) - y[0] * np.log(y[0])  # z' = z*cos(x) - y*ln(y)
    return np.vstack((z, dzdx))

def bc(ya, yb):
    return np.array([ya[0] - 1, yb[0] - np.exp(1)])  # Boundary conditions y(0) = 1, y(pi/2) = e

# Define the exact solution for comparison
def exact1(x):
    return np.exp(np.sin(x))

# Initial mesh points for the solution
x_mesh = np.linspace(0, np.pi/2, 10)
y_mesh = np.ones((2, x_mesh.size))  # Initial guess for y and z

# Solve the boundary value problem
sol = solve_bvp(ode_system, bc, x_mesh, y_mesh)

# Generate points for plotting
x_plot = np.linspace(0, np.pi/2, 100)
y_plot = sol.sol(x_plot)[0]  # Extracting y values from the solution

# Plotting the result
plt.figure(figsize=(5, 4))
plt.plot(x_plot, y_plot, label='Numerical Solution')
plt.plot(x_plot, exact1(x_plot), label='Exact Solution', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Solution to y'' = y'cos(x) - y ln(y), y(0) = 1, y(pi/2) = e")

plt.legend()
plt.grid(True)
plt.show()

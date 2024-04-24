# 8(1)
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the function y' = te^(3t) - 2y
def F1(t, y):
    return t * np.exp(3*t) - 2*y

# Define the exact solution for comparison
def exact1(t):
    return (np.exp(-2*t) + np.exp(3*t)*(5*t - 1))/25 # evaluated from WolframAlpha

# Initial condition
t0 = 0
y0 = 0

# Define the time span
t_span = (0, 1)

# Solve using solve_ivp
sol = solve_ivp(F1, t_span, [y0], t_eval=np.linspace(0, 1, 100))

# Extract the solution
t_values = sol.t
y_values = sol.y[0]

# Plotting the result
plt.figure(figsize=(5, 4))
plt.plot(t_values, y_values, label='Numerical Solution')
plt.plot(t_values, exact1(t_values), label='Exact Solution', linestyle='--')
plt.xlabel('t')
plt.ylabel('y')
plt.grid(True)
plt.title("Solution to y' = te^(3t) - 2y, y(0) = 0")
plt.legend()

plt.show()

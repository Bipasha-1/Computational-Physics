#14.
import numpy as np
import matplotlib.pyplot as plt

# Define the differential equation
def f(t, y):
    return (2*t*y[1] - 2*y[0] + t**3 * np.log(t)) / t**2

# Define the exact solution
def exact_solution(t):
    return 7*t/4 + 0.5*(t**3) * np.log(t) - 0.75*t**3

# Euler's method
def euler_method(f, t0, y0, yp0, h, num_steps):
    t_values = [t0]
    y_values = [[y0, yp0]]  # Store [y, yp] pairs

    for _ in range(num_steps):
        t = t_values[-1]
        y = y_values[-1][0]  # Extract y from [y, yp]
        yp = y_values[-1][1]  # Extract yp from [y, yp]

        # Calculate the next values
        y_next = y + h * yp
        yp_next = yp + h * f(t, [y, yp])

        # Append [y, yp] to the lists
        t_values.append(t + h)
        y_values.append([y_next, yp_next])

    return t_values, y_values

# Parameters
t0 = 1  # Initial t
y0 = 1  # y(1) = 1
yp0 = 0  # y'(1) = 0
h = 0.001  # Step size
num_steps = int((2 - t0) / h)  # Number of steps to reach t=2

# Perform Euler's method
t_values, y_values = euler_method(f, t0, y0, yp0, h, num_steps)

# Extract y values
approx_y_values = [y[0] for y in y_values]

# Calculate the exact solution for plotting
t_exact = np.linspace(1, 2, 1000)
y_exact = exact_solution(t_exact)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t_values, approx_y_values, label='Euler\'s Method Approximation', color='blue')
plt.plot(t_exact, y_exact, label='Exact Solution', color='red', linestyle='--')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Euler\'s Method Approximation vs. Exact Solution')
plt.legend()
plt.grid(True)
plt.show()

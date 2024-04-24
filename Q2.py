#2.
import numpy as np
import matplotlib.pyplot as plt

def backward_euler(dy_dt, t0, y0, h, t_target):
    t_values = [t0]
    y_values = [y0]
    
    while t_values[-1] < t_target:
        t_new = t_values[-1] + h
        y_new = y_values[-1] + h * dy_dt(t_values[-1], y_values[-1])
        t_values.append(t_new)
        y_values.append(y_new)
    
    return t_values, y_values

# Define the first initial value problem: dy/dx = y/t-(y/t)^2, y(1) = 1
def f1(t, y):
    return y/t-(y/t)**2

# Define the exact solution for the first problem
def exact1(t):
    return t/(1+np.log(t)) 

# Solve the first initial value problem
t_values1, y_values1 = backward_euler(f1, 1, 1, 0.1, 2)

# Calculate absolute and relative errors
absolute_errors1 = [abs(exact1(t) - y) for t, y in zip(t_values1, y_values1)]
relative_errors1 = [abs((exact1(t) - y) / exact1(t)) for t, y in zip(t_values1, y_values1)]

# Plotting the results
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(t_values1, y_values1, label="Approximation")
plt.plot(t_values1, [exact1(t) for t in t_values1], label="Exact Solution")
plt.xlabel('t')
plt.ylabel('y')
plt.title('Solution to dy/dx = y/t-(y/t)^2 with y(1) = 1')
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t_values1, absolute_errors1, label="Absolute Error")
plt.plot(t_values1, relative_errors1, label="Relative Error")
plt.xlabel('t')
plt.ylabel('Error')
plt.title("Absolute and Relative Errors")
plt.legend()

plt.tight_layout()
plt.show()
print("Absolute Errors:")
for i, t in enumerate(t_values1):
    print(f"At t = {t:.2f}, Absolute Error = {absolute_errors1[i]:.6f}")

print("\nRelative Errors:")
for i, t in enumerate(t_values1):
    print(f"At t = {t:.2f}, Relative Error = {relative_errors1[i]:.6f}")

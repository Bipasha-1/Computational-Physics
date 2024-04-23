#1
def backward_euler(dy_dx, x0, y0, h, x_target):
    """
    Backward Euler's Method for solving dy/dx = f(x, y)
    with an initial condition y(x0) = y0.
    
    Args:
        dy_dx: The function f(x, y) representing dy/dx.
        x0: Initial x value.
        y0: Initial y value.
        h: Step size.
        x_target: The x value where we want to find y.
    
    Returns:
        x_values: List of x values.
        y_values: List of corresponding y values.
    """
    x_values = [x0]
    y_values = [y0]
    
    while x_values[-1] < x_target:
        x_new = x_values[-1] + h
        y_new = y_values[-1] + h * dy_dx(x_values[-1], y_values[-1])
        x_values.append(x_new)
        y_values.append(y_new)
    
    return x_values, y_values

# Define the first initial value problem: dy/dx = -9y, y(0) = e
def f1(x, y):
    return -9 * y

# Solve the first initial value problem
x_values1, y_values1 = backward_euler(f1, 0, np.exp(1), 0.01, 1)

# Define the second initial value problem: dy/dx = -20(y - x)^2 + 2x, y(0) = 1/3
def f2(x, y):
    return -20 * (y - x)**2 + 2 * x

# Solve the second initial value problem
x_values2, y_values2 = backward_euler(f2, 0, 1/3, 0.01, 1)

# Plotting the results
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(x_values1, y_values1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution to dy/dx = -9y, y(0) = e')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x_values2, y_values2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution to dy/dx = -20(y - x)^2 + 2x, y(0) = 1/3')
plt.grid(True)

plt.tight_layout()
plt.show()


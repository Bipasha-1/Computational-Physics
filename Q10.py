#10.
def rk4_step(f, t, y, h):
    """
    Single step of the 4th-order Runge-Kutta method.
    
    Args:
        f: Function representing the derivative dy/dt.
        t: Current time t.
        y: Current value y.
        h: Step size.
    
    Returns:
        y_next: Next value of y.
    """
    k1 = h * f(t, y)
    k2 = h * f(t + h/2, y + k1/2)
    k3 = h * f(t + h/2, y + k2/2)
    k4 = h * f(t + h, y + k3)
    
    y_next = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    return y_next

def adaptive_rk4(f, t0, y0, t_end, tol):
    """
    Adaptive step-size 4th Order Runge-Kutta Method for solving an ODE.
    
    Args:
        f: Function representing the derivative dy/dt.
        t0: Initial time.
        y0: Initial value of y.
        t_end: End time.
        tol: Desired absolute accuracy.
    
    Returns:
        t_values: List of time values.
        y_values: List of corresponding y values.
    """
    t_values = [t0]
    y_values = [y0]
    
    t = t0
    y = y0
    h = 0.1  # Initial step size
    
    while t < t_end:
        y1 = rk4_step(f, t, y, h)  # Take one full step
        y2_half = rk4_step(f, t, y, h/2)  # Take two half steps
        y2 = rk4_step(f, t + h/2, y2_half, h/2)
        
        # Error estimation
        error = np.abs(y2 - y1)
        
        # Update step size
        h_new = h * np.sqrt(tol / (2 * error))
        
        # Adjust step size if necessary
        if h_new > 2 * h:
            h_new = 2 * h
        elif h_new < 0.5 * h:
            h_new = 0.5 * h
        
        # Update values
        t = t + h
        y = y2
        h = h_new
        
        # Append to lists
        t_values.append(t)
        y_values.append(y)
    
    return t_values, y_values

def ode(t, y):
    return (y**2 + y) / t

# Initial condition
t0 = 1
y0 = -2

# End time
t_end = 3

# Desired absolute accuracy
tol = 1e-4

# Solve using adaptive step-size RK4 method
t_values, y_values = adaptive_rk4(ode, t0, y0, t_end, tol)

# Plotting the result
plt.figure(figsize=(8, 5))
plt.plot(t_values, y_values, label='Solution')
plt.scatter(t_values, y_values, c='r', label='Mesh Points')
plt.xlabel('t')
plt.ylabel('y')
plt.title("Solution to y' = (y^2 + y)/t with adaptive step-size control")
plt.legend()
plt.grid(True)
plt.show()

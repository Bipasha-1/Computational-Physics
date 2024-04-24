# 12
def rk4_system(f, t0, u0, t_end, h):
    """
    4th Order Runge-Kutta Method for solving a system of ODEs.
    
    Args:
        f: Function representing the system of ODEs, f(t, u).
        t0: Initial time.
        u0: Initial values of the system [u1(0), u2(0), u3(0)].
        t_end: End time.
        h: Step size.
    
    Returns:
        t_values: List of time values.
        u_values: List of corresponding u values for each component [u1, u2, u3].
    """
    t_values = [t0]
    u_values = [u0]
    
    t = t0
    u = u0
    
    while t < t_end:
        k1 = h * f(t, u)
        k2 = h * f(t + h/2, u + k1/2)
        k3 = h * f(t + h/2, u + k2/2)
        k4 = h * f(t + h, u + k3)
        
        u_next = u + (k1 + 2*k2 + 2*k3 + k4) / 6
        t = t + h
        
        t_values.append(t)
        u_values.append(u_next)
        
        u = u_next
    
    return t_values, np.array(u_values)

def system(t, u):
    u1 = u[0]
    u2 = u[1]
    u3 = u[2]
    
    du1_dt = u1 + 2*u2 - 2*u3 + np.exp(-t)
    du2_dt = u2 + u3 - 2*np.exp(-t)
    du3_dt = u1 + 2*u2 + np.exp(-t)
    
    return np.array([du1_dt, du2_dt, du3_dt])

# Initial conditions
t0 = 0
u0 = np.array([3, -1, 1])

# End time
t_end = 1

# Step size
h = 0.01

# Solve using RK4 method
t_values, u_values = rk4_system(system, t0, u0, t_end, h)

# Extract u1, u2, u3 values
u1_values = u_values[:, 0]
u2_values = u_values[:, 1]
u3_values = u_values[:, 2]

# Plotting the result
plt.figure(figsize=(10, 6))
plt.plot(t_values, u1_values, label='u1')
plt.plot(t_values, u2_values, label='u2')
plt.plot(t_values, u3_values, label='u3')
plt.xlabel('t')
plt.ylabel('u')
plt.title("Solution to the System of ODEs")
plt.legend()
plt.grid(True)
plt.show()

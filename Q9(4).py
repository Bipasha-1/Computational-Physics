#9(4)
def ode_system(x, y):
    z = y[1]  # y' = z
    dzdx = 1/2 - 2*(z/2)**2 - y[0]*np.sin(x)/2  # z' = 1/2 - (z/2)^2 - y*sin(x)/2
    return np.vstack((z, dzdx))

def bc(ya, yb):
    return np.array([ya[0] - 2, yb[0] - 2])  # Boundary conditions y(0) = 2, y(pi) = 2

# Initial mesh points for the solution
x_mesh = np.linspace(0, np.pi, 10)
y_mesh = np.ones((2, x_mesh.size)) * 2  # Initial guess for y and z

# Solve the boundary value problem
sol = solve_bvp(ode_system, bc, x_mesh, y_mesh)

# Generate points for plotting
x_plot = np.linspace(0, np.pi, 100)
y_plot = sol.sol(x_plot)[0]  # Extracting y values from the solution

# Plotting the result
plt.figure(figsize=(5, 4))
plt.plot(x_plot, y_plot, label='Numerical Solution')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Solution to y'' = 1/2 - (y')^2/2 - y*sin(x)/2, y(0) = 2, y(pi) = 2")

plt.legend()
plt.grid(True)
plt.show()

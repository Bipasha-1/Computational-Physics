# 8(4)
def F4(t, y):
    return  np.cos(2*t) + np.sin(3*t)

# Define the exact solution for comparison
def exact1(t):
    return (8-2*np.cos(3*t) + 3*np.sin(2*t))/6 # evaluated from WolframAlpha

# Initial condition
t0 = 0
y0 = 1

# Define the time span
t_span = (0, 1)

# Solve using solve_ivp
sol = solve_ivp(F4, t_span, [y0], t_eval=np.linspace(0, 1, 100))

# Extract the solution
t_values = sol.t
y_values = sol.y[0]

# Plotting the result
plt.figure(figsize=(5, 4))
plt.plot(t_values, y_values, label='Numerical Solution')
plt.plot(t_values, exact1(t_values), label='Exact Solution', linestyle='--')
plt.xlabel('t')
plt.ylabel('y')
plt.title("Solution to y' = cos 2t + sin 3t, y(0) = 1")
plt.grid(True)
plt.legend()

plt.show()

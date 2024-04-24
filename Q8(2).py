# 8(2): Define the function y' = 1 - (t - y)^2
def F2(t, y):
    return 1 - (t - y)**2

# Initial condition
t0 = 2
y0 = 1

# Define the time span
t_span = (2, 3)

# Solve using solve_ivp
sol = solve_ivp(F2, t_span, [y0], t_eval=np.linspace(2, 3, 100))

# Extract the solution
t_values = sol.t
y_values = sol.y[0]

# Plotting the result
plt.figure(figsize=(5, 4))
plt.grid(True)
plt.plot(t_values, y_values)
plt.xlabel('t')
plt.ylabel('y')
plt.title("Solution to y' = 1 - (t - y)^2, y(2) = 1")
plt.legend()

plt.show()

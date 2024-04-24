# 8(1): Define the function y' = te^(3t))-2y
def F1(t, y):
    return  t*(np.exp(3*t))-2*y

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
plt.plot(t_values, y_values)
plt.xlabel('t')
plt.ylabel('y')
plt.grid(True)
plt.title("Solution to y' = te^(3t))-2y, y(0) = 0")
plt.legend()

plt.show()

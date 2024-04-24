# 8(3)
def F3(t, y):
    return  1 + y/t

# Define the exact solution for comparison
def exact1(t):
    return t*(2+np.log(t)) # evaluated from WolframAlpha

# Initial condition
t0 = 1
y0 = 2

# Define the time span
t_span = (1, 2)

# Solve using solve_ivp
sol = solve_ivp(F3, t_span, [y0], t_eval=np.linspace(1, 2, 100))

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
plt.title("Solution to y' = 1 +y/t, y(1) = 2")
plt.legend()

plt.show()

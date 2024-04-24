# 11.
# Runge Kutta Method 4
# u=t/(t+1)
def F(x, u):
    return 1/((x*(1-u))**2+u**2)

a = 0
b = 0.9999997142857959  # Corresponding to t=3.5* 10^6
N =100
h = (b-a)/N

upoints = np.arange(a,b,h)

xpoints = []

x = 1.0
tpoints= [u/(1-u) for u in upoints]

for u in upoints:
    xpoints.append(x)

    k1 = h*F(x, u)  

    k2 = h*F(x+0.5*k1, u+0.5*h)

    k3 = h*F(x+0.5*k2, u+0.5*h)

    k4 = h*F(x+k3, u+h)

    x += (k1 + 2*k2 + 2*k3 + k4)/6
    
plt.figure(figsize=(12, 4))    

plt.subplot(1, 2, 1)    
plt.plot(upoints, xpoints)
plt.xlabel('u')
plt.ylabel('x')
plt.title('x(u) vs u')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(tpoints, xpoints)
plt.xlabel('t')
plt.ylabel('x')
plt.title('x(t) vs t')
plt.grid(True)

plt.show()
print(xpoints[-1])

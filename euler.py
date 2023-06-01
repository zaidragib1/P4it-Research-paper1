import numpy as np
import matplotlib.pyplot as plt

# Define the differential equation to solve
def dydx(x, y):
    return x - 2 * y

# Define the analytical solution (for comparison)
def y_analytical(x):
    return 0.5 * np.array(x) - 0.25 + 0.75 * np.exp(-2 * np.array(x))

# Define the RK2 method
def rk2_step(x, y, h, dydx):
    k1 = h * dydx(x, y)
    k2 = h * dydx(x + h/2, y + k1/2)
    y_next = y + k2
    return y_next

# Define the Euler method
def euler_step(x, y, h, dydx):
    y_next = y + h * dydx(x, y)
    return y_next

# Define the initial conditions and step size
x0 = 0
y0 = 0
h = 0.1
xmax = 1

# Initialize the numerical solutions and errors
x = [x0]
y_rk2 = [y0]
y_euler = [y0]
error_rk2 = [0]
error_euler = [0]

# Apply the RK2 and Euler methods to obtain the numerical solutions and errors
while x[-1] < xmax:
    y_rk2_next = rk2_step(x[-1], y_rk2[-1], h, dydx)
    y_euler_next = euler_step(x[-1], y_euler[-1], h, dydx)
    x.append(x[-1] + h)
    y_rk2.append(y_rk2_next)
    y_euler.append(y_euler_next)
    error_rk2.append(y_analytical(x[-1]) - y_rk2[-1])
    error_euler.append(y_analytical(x[-1]) - y_euler[-1])

# Plot the numerical solutions and errors
fig, ax = plt.subplots(2, 1, figsize=(8, 8))

ax[0].plot(x, y_rk2, label='RK2 method')
ax[0].plot(x, y_euler, label='Euler method')
ax[0].plot(x, y_analytical(x), label='Analytical solution')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[0].set_title('Numerical solutions')
ax[0].legend()

ax[1].plot(x, error_rk2, label='RK2 method')
ax[1].plot(x, error_euler, label='Euler method')
ax[1].set_xlabel('x')
ax[1].set_ylabel('Error')
ax[1].set_title('Errors')
ax[1].legend()

plt.show()

# Calculate the maximum absolute errors and the RMSEs
max_abs_error_rk2 = max(abs(error_rk2))
max_abs_error_euler = max(abs(error_euler))
rmse_rk2 = np.sqrt(np.mean(np.array(error_rk2)**2))
rmse_euler = np.sqrt(np.mean(np.array(error_euler)**2))
print('RK2 method:')
print(f'Maximum absolute error: {max_abs_error_rk2}')
print(f'RMSE: {rmse_rk2}')
print('Euler method:')
print(f'Maximum absolute error: {max_abs_error_euler}')
print(f'RMSE: {rmse_euler}')

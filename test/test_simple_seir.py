from Epidemic import simple_dynamics
import numpy as np
import matplotlib.pyplot as plt

N = 1000000
D = 4.0
gamma = 1.0 / D
delta = 1.0 / 5.0
R_0 = 5.0
beta = R_0 * gamma

S0, E0, I0, R0 = N-1, 1, 0, 0

t = np.linspace(0, 100, 100)
y0 = S0, E0, I0, R0

S, E, I, R = simple_dynamics.solve_SEIR(y0, t, N, beta, gamma, delta)


fig, ax = plt.subplots()
ax.plot(t, S, label='Susceptible')
ax.plot(t, E, label='Exposed')
ax.plot(t, I, label='Infected')
ax.plot(t, R, label='Recovered')
ax.legend()
plt.show()


import numpy as np
from scipy.integrate import odeint


def _ode_SEIR(y, t, N, beta, gamma, delta):
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - delta * E
    dIdt = delta * E - gamma * I
    dRdt = gamma * I
    return(dSdt, dEdt, dIdt, dRdt)


def solve_SEIR(y0, t, N, beta, gamma, delta):
    ret = odeint(_ode_SEIR, y0, t, args=(N, beta, gamma, delta))
    S, E, I, R = ret.T
    return(S, E, I, R)
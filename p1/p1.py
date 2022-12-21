import numpy as np
import math
from time import sleep

IP = "Adress"
NP = "N port"
NT = "abotcmd"
SP = 10
SG = 10
U = 0


def distance(a, b):
    x = b[0] - a[0]
    y = b[1] - a[1]
    g = (x**2 + y**2)**(1/2)
    return g


def time(g, SP):
    t = g / SP
    return t


def grUgol(a, b):
    x = b[0] - a[0]
    y = b[1] - a[1]

    if y >= 0:
        l = 1
    else:
        l = 0

    if x >= 0:
        o = 1
    else:
        o = 0

    g = (x ** 2 + y ** 2) ** (1 / 2)
    if y != 0:
        k1 = y / g
        k2 = math.asin(k1)
        k3 = math.degrees(k2)

    else:
        k3 = 0

    if l == 1:
        if o == 1:
            k3 = k3
        else:
            k3 = 180 - k3
    else:
        if o == 1:
            k3 = k3
        else:
            k3 = -180 - k3

    k3 -=U

    return k3


def grtime(Ugol):
    tug = abs(Ugol / SG)
    return tug


file_data = np.loadtxt("p1.txt")
print(file_data)

for i in range(len(file_data)-1):
    dist = distance(file_data[i], file_data[i+1])
    T_T = time(dist, SP)
    Ugol = grUgol(file_data[i], file_data[i + 1])
    U += Ugol
    TU = grtime(Ugol)
    print('{"cmd": "turn", "val": ' + str(Ugol) + '}')
    sleep(TU)
    print('{"cmd": "move", "val": ' + str(dist)+ '}')
    sleep(T_T)

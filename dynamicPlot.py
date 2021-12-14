#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ----------- initialisation var ----------------

xmin = -5  # Borne inf des abscisses
xmax = 5  # Borne Sup des abscisses
nbx = 150  # facteur de lissage de la courbe
dt = 0.1  # facteur de variation dans le temps
z = np.linspace(0, 0, nbx)

# ----------- initialisation graphe -----------

fig = plt.figure()  # initialise la figure
(line,) = plt.plot([], [], "r", label="sinus")
(line2,) = plt.plot([], [], "b", label="")
plt.ylim(-1, 1)  # initialise les bornes des ordonnees
plt.xlabel("abscisses")
plt.ylabel("ordonnees")


def animate(i):
    t = i * dt
    plt.xlim(xmin + t, xmax + t)  # les bornes varient avec le temps
    x = np.linspace(xmin + t, xmax + t, nbx)  # MAJ domaine des abscisses
    y = [np.sin(a) for a in x]  # ou y = np.sin(x)
    line.set_data(x, y)
    line2.set_data(x, z)
    # return (line,)


ani = animation.FuncAnimation(
    fig, animate, frames=300, blit=False, interval=80, repeat=True
)

plt.legend()  # afficher la legende
plt.grid()  # afficher en grilles
plt.show()

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def df(x):
    return np.cos(x)

x = np.linspace(0, 2*np.pi, 400)
y = f(x)

points = [0, np.pi/4, np.pi/2, np.pi, 3*np.pi/2]
labels = ['0', 'π/4', 'π/2', 'π', '3π/2']
colors = ['red', 'green', 'blue', 'magenta', 'cyan']

plt.figure(figsize=(10, 6))

plt.plot(x, y, color='black', linewidth=3, label='f(x) = sin(x)')

delta = np.pi / 3

for x0, lbl, color in zip(points, labels, colors):
    y0 = f(x0)
    slope = df(x0)

    x_tan = np.linspace(x0 - delta, x0 + delta, 100)
    y_tan = y0 + slope * (x_tan - x0)

    plt.plot(x_tan, y_tan, color=color, linewidth=2,
             label=f'Tangente en x = {lbl}')
    plt.scatter(x0, y0, color=color, s=80, zorder=5)


plt.title('Rectas tangentes a f(x) = sin(x)', fontweight='bold')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("grafico_tangentes.png", dpi = 300)
plt.show()

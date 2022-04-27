"""
One constant vector in the middle (rotating at a frequency of 0). Notated as e^(0*2*pi*i*t).
One vector that rotates 1 time per second. Notated as e^(2*pi*i*t).
One vector that rotates -1 time per second. Notated as e^(-2*pi*i*t).
One vector that rotates 2 times per second. Notated as e^(2*2*pi*i*t).
General formula: e^(n*2*pi*i*t)
Control the initial size and rotation of each vector by changing the values of the constants. Notated as cn.
To change the initial size of the vectors, use a real number as the constant.
To change the initial rotation of the vectors, use a complex number as the constant. Notated as e^((pi*something)*i).
To change both the initial size and rotation of the vectors, use a real number times a complex number as the constant. Notated as real*e^((pi*something)*i).
To approximate c0 (the constant term in front of the constant vector), take the average of a sampling of values from the function. More points = more accurate.
In other words, c0 = Integral from 0 to Max(t) of f(t)dt.
General formula: cn = Integral from 0 to Max(t) of f(t) * e^(-n*2*pi*i*t)dt.
Consider using an svg file to get sample points for the function.
"""

"""
Example Shapes:

Upside down water droplet:
x_data.append(math.sin(i)*math.cos(i)*math.log(abs(i)))
y_data.append((abs(i)**0.3) * (math.cos(i)**(1/2)))

Heart:
x_data.append(0.75*(2 * (1 + math.cos(i)) * math.sin(i)))
y_data.append(-(2 * (1 + math.cos(i)) * math.cos(i)))

Italicized 8:
x_data.append(math.sin(i)*math.cos(i)*math.log(abs(i)))
y_data.append(2 * (1 + math.cos(i)) * math.sin(i))
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
x_data = []
y_data = []

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
line, = ax.plot(0, 0)


def animation_frame(i):
    x_data.append(0.75*(2 * (1 + math.cos(i)) * math.sin(i)))
    y_data.append(-(2 * (1 + math.cos(i)) * math.cos(i)))

    line.set_data(x_data, y_data)
    return line,


animation = FuncAnimation(fig, func=animation_frame,
                          frames=np.arange(1, 90, 0.1), interval=10)
plt.show()

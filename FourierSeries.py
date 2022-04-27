"""
One constant vector in the middle (rotating at a frequency of 0). Notated as e^(0*2*pi*i*t).
One vector that rotates 1 time per second. Notated as e^(1*2*pi*i*t).
One vector that rotates -1 time per second. Notated as e^(-1*2*pi*i*t).
One vector that rotates 2 times per second. Notated as e^(2*2*pi*i*t).
General formula: e^(n*2*pi*i*t)
Control the initial size and rotation of each vector by changing the values of the constants. Notated as cn.
To change the initial size of the vectors, use a real number as the constant.
To change the initial rotation of the vectors, use a complex number as the constant. Notated as e^((pi*something)*i).
To change both the initial size and rotation of the vectors, use a real number times a complex number as the constant. Notated as real*e^((pi*something)*i).
To approximate c0 (the constant term in front of the constant vector), take the average of a sampling of values from the function. More points = more accurate.
In other words, c0 = Integral from 0 to Max(t) of f(t)dt.
General formula: cn = Integral from 0 to Max(t) of f(t) * e^(-2*pi*i*n*t)dt.
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


from numbers import Complex
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
from svgpathtools import parse_path
from sympy import true
i = complex(0, 1)


def findN(loop):
    if loop == 0:
        return 0
    elif loop % 2 == 0:
        return int(-1 * (loop / 2))
    else:
        return int((loop + 1) / 2)


def estimatePoint(vectors, t):
    point = complex(0, 0)
    for j in range(len(vectors)):
        coefficient = vectors[j]["coefficient"]
        eTerm = math.e ** (findN(j) * 2 * math.pi * i * t)
        point += coefficient * eTerm
    return point


while True:
    userInput = input("Enter a function: ")

    if userInput == "Display L":

        x_data = []
        y_data = []

        path = parse_path("M 283.072 92.577 C 259.529 92.577 235.987 92.577 212.444 92.577 C 207.025 92.577 201.605 92.407 196.188 92.577 C 193.939 92.648 191.053 91.255 189.462 93.297 C 188.43 94.621 191.301 96.207 192.265 97.613 C 195.412 102.203 198.629 106.714 201.794 111.283 C 215.072 130.455 229.416 148.499 241.592 168.84 C 242.531 170.408 238.612 169.85 237.108 170.278 C 233.566 171.288 230.04 172.424 226.457 173.156 C 221.811 174.104 209.505 170.6 212.444 175.314 C 219.67 186.909 232.306 190.544 242.152 198.338 C 254.728 208.291 267.395 218.074 279.709 228.555 C 285.159 233.194 290.343 238.348 295.404 243.664 C 296.533 244.849 299.175 246.581 298.206 247.98 C 296.55 250.371 293.411 250.036 290.919 250.138 C 281.767 250.517 272.608 249.681 263.453 249.419 C 262.706 249.397 264.995 249.082 265.695 249.419 C 268.042 250.549 270.16 252.348 272.422 253.736 C 278.756 257.624 284.975 261.855 291.48 265.247 C 308.904 274.333 326.588 282.575 344.17 291.149 C 350.692 294.328 357.197 297.573 363.789 300.502 C 366.918 301.891 371.837 307.898 373.318 304.097 C 374.923 299.977 368.924 296.808 366.592 293.306 C 359.02 281.937 351.653 270.315 343.61 259.491 C 340.043 254.691 327.488 250.12 331.839 246.541 C 341.341 238.723 354.499 244.903 365.471 241.504 C 366.793 241.095 365.389 237.595 364.35 236.469 C 348.386 219.168 331.323 203.602 315.022 186.827 C 310.579 182.255 306.433 177.225 302.13 172.437 C 300.828 170.989 297.13 169.846 298.206 168.12 C 300.018 165.213 303.74 165.748 306.614 165.242 C 313.301 164.063 320.057 163.613 326.794 163.085 C 329.218 162.894 332.995 165.873 334.081 163.085 C 335.087 160.5 330.546 159.47 329.036 157.327 C 326.98 154.412 325.415 150.973 323.431 147.974 C 313.828 133.462 303.999 119.197 294.283 104.807 L 283.072 92.577")

        fig, ax = plt.subplots()
        ax.set_xlim(150, 400)
        ax.set_ylim(-350, -50)
        line, = ax.plot(0, 0)

        def animation_frame(i):
            x_data.append(path.point(i/100).real)
            y_data.append(-(path.point(i/100).imag))

            line.set_data(x_data, y_data)
            return line,

        animation = FuncAnimation(fig, func=animation_frame,
                                  frames=np.arange(1, 100, 0.1), interval=10)
        plt.show()

        # Initialize starting data
        path = parse_path("M 283.072 92.577 C 259.529 92.577 235.987 92.577 212.444 92.577 C 207.025 92.577 201.605 92.407 196.188 92.577 C 193.939 92.648 191.053 91.255 189.462 93.297 C 188.43 94.621 191.301 96.207 192.265 97.613 C 195.412 102.203 198.629 106.714 201.794 111.283 C 215.072 130.455 229.416 148.499 241.592 168.84 C 242.531 170.408 238.612 169.85 237.108 170.278 C 233.566 171.288 230.04 172.424 226.457 173.156 C 221.811 174.104 209.505 170.6 212.444 175.314 C 219.67 186.909 232.306 190.544 242.152 198.338 C 254.728 208.291 267.395 218.074 279.709 228.555 C 285.159 233.194 290.343 238.348 295.404 243.664 C 296.533 244.849 299.175 246.581 298.206 247.98 C 296.55 250.371 293.411 250.036 290.919 250.138 C 281.767 250.517 272.608 249.681 263.453 249.419 C 262.706 249.397 264.995 249.082 265.695 249.419 C 268.042 250.549 270.16 252.348 272.422 253.736 C 278.756 257.624 284.975 261.855 291.48 265.247 C 308.904 274.333 326.588 282.575 344.17 291.149 C 350.692 294.328 357.197 297.573 363.789 300.502 C 366.918 301.891 371.837 307.898 373.318 304.097 C 374.923 299.977 368.924 296.808 366.592 293.306 C 359.02 281.937 351.653 270.315 343.61 259.491 C 340.043 254.691 327.488 250.12 331.839 246.541 C 341.341 238.723 354.499 244.903 365.471 241.504 C 366.793 241.095 365.389 237.595 364.35 236.469 C 348.386 219.168 331.323 203.602 315.022 186.827 C 310.579 182.255 306.433 177.225 302.13 172.437 C 300.828 170.989 297.13 169.846 298.206 168.12 C 300.018 165.213 303.74 165.748 306.614 165.242 C 313.301 164.063 320.057 163.613 326.794 163.085 C 329.218 162.894 332.995 165.873 334.081 163.085 C 335.087 160.5 330.546 159.47 329.036 157.327 C 326.98 154.412 325.415 150.973 323.431 147.974 C 313.828 133.462 303.999 119.197 294.283 104.807")
        x_data = []
        y_data = []
        samplePoints = int(input(
            "Enter the number of sample points to be taken for vector estimations: "))
        step = 1 / samplePoints
        numberOfVectors = int(
            input("Enter the number of vectors to be used in function estimations: "))
        fig, ax = plt.subplots()
        ax.set_xlim(-150, 150)
        ax.set_ylim(-150, 150)
        line, = ax.plot(0, 0)
        i = complex(0, 1)

        # Calculate the coefficients of the vectors
        vectorCoefficients = [None] * numberOfVectors
        for temp in range(numberOfVectors):
            if temp == 0:
                n = 0
            elif temp % 2 == 0:
                n = int(-1 * (temp / 2))
            else:
                n = int((temp + 1) / 2)

            # Reset the x and y data
            totalX, totalY = 0, 0
            # Calculate the average of the sample points
            for j in range(samplePoints):
                t = j * step
                point = (math.e**(-2*math.pi*i*n*t)) * (path.point(t))
                totalX += point.real - 300
                totalY += -(point.imag) + 200
            averageX = (totalX / samplePoints).real
            averageY = (totalY / samplePoints).real

            vectorLength = math.sqrt(averageX**2 + averageY**2)

            if averageX > 0:
                radians = math.atan(averageY / averageX)
            elif averageX == 0:
                radians = math.pi / 2
            else:
                radians = math.atan(averageY / averageX) + math.pi

            vectorCoefficients[temp] = vectorLength * \
                (math.e**(complex(0, radians)))

        # Animation
        def animation_frame(t):
            finalPoint = complex(0, 0)

            for temp in range(numberOfVectors):
                if temp == 0:
                    n = 0
                elif temp % 2 == 0:
                    n = int(-1 * (temp / 2))
                else:
                    n = int((temp + 1) / 2)

                coefficient = vectorCoefficients[temp]
                finalPoint += (coefficient * (math.e**(n*2*math.pi*i*t)))

            x_data.append(finalPoint.real - 300)
            y_data.append((finalPoint.imag) + 200)

            line.set_data(x_data, y_data)
            return line,

        animation = FuncAnimation(fig, func=animation_frame,
                                  frames=np.arange(1, 100, 0.01), interval=10)
        plt.show()

    elif userInput == "Estimate L":
        while True:
            x_data = []
            y_data = []

            path = parse_path("M 283.072 92.577 C 259.529 92.577 235.987 92.577 212.444 92.577 C 207.025 92.577 201.605 92.407 196.188 92.577 C 193.939 92.648 191.053 91.255 189.462 93.297 C 188.43 94.621 191.301 96.207 192.265 97.613 C 195.412 102.203 198.629 106.714 201.794 111.283 C 215.072 130.455 229.416 148.499 241.592 168.84 C 242.531 170.408 238.612 169.85 237.108 170.278 C 233.566 171.288 230.04 172.424 226.457 173.156 C 221.811 174.104 209.505 170.6 212.444 175.314 C 219.67 186.909 232.306 190.544 242.152 198.338 C 254.728 208.291 267.395 218.074 279.709 228.555 C 285.159 233.194 290.343 238.348 295.404 243.664 C 296.533 244.849 299.175 246.581 298.206 247.98 C 296.55 250.371 293.411 250.036 290.919 250.138 C 281.767 250.517 272.608 249.681 263.453 249.419 C 262.706 249.397 264.995 249.082 265.695 249.419 C 268.042 250.549 270.16 252.348 272.422 253.736 C 278.756 257.624 284.975 261.855 291.48 265.247 C 308.904 274.333 326.588 282.575 344.17 291.149 C 350.692 294.328 357.197 297.573 363.789 300.502 C 366.918 301.891 371.837 307.898 373.318 304.097 C 374.923 299.977 368.924 296.808 366.592 293.306 C 359.02 281.937 351.653 270.315 343.61 259.491 C 340.043 254.691 327.488 250.12 331.839 246.541 C 341.341 238.723 354.499 244.903 365.471 241.504 C 366.793 241.095 365.389 237.595 364.35 236.469 C 348.386 219.168 331.323 203.602 315.022 186.827 C 310.579 182.255 306.433 177.225 302.13 172.437 C 300.828 170.989 297.13 169.846 298.206 168.12 C 300.018 165.213 303.74 165.748 306.614 165.242 C 313.301 164.063 320.057 163.613 326.794 163.085 C 329.218 162.894 332.995 165.873 334.081 163.085 C 335.087 160.5 330.546 159.47 329.036 157.327 C 326.98 154.412 325.415 150.973 323.431 147.974 C 313.828 133.462 303.999 119.197 294.283 104.807 L 283.072 92.577")

            fig, ax = plt.subplots()
            ax.set_xlim(150, 400)
            ax.set_ylim(-350, -50)
            line, = ax.plot(0, 0)

            # Create array of vectors
            vectors = [
                None] * int(input("Enter the number of vectors to be used in function estimations: "))

            step = 1 / 100
            for j in range(len(vectors)):
                n = findN(j)
                addedPoints = complex(0, 0)
                # Calculate average point
                for k in range(100):
                    t = k * step
                    actualValue = path.point(t)
                    eTerm = (math.e**(-2*math.pi*i*n*t))
                    addedPoints += (eTerm * actualValue)
                averagePoint = addedPoints / 100
                vectors[j] = {"coefficient": averagePoint}

            def animation_frame(t):
                x_data.append(estimatePoint(vectors, t).real)
                y_data.append(-(estimatePoint(vectors, t).imag))

                line.set_data(x_data, y_data)
                return line,

            animation = FuncAnimation(fig, func=animation_frame,
                                      frames=np.arange(1, 100, 0.01), interval=10)
            plt.show()

    elif userInput == "Display H":

        x_data = []
        y_data = []

        fig, ax = plt.subplots()
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        line, = ax.plot(0, 0)

        def animation_frame(i):
            x_data.append(0.75*(2 * (1 + math.cos(i)) * math.sin(i)))
            y_data.append(-(2 * (1 + math.cos(i)) * math.cos(i)))

            line.set_data(x_data, y_data)
            return line,

        animation = FuncAnimation(fig, func=animation_frame,
                                  frames=np.arange(1, 100, 0.05), interval=10)
        plt.show()

    elif userInput == "Estimate H":
        while True:
            x_data = []
            y_data = []

            fig, ax = plt.subplots()
            ax.set_xlim(-5, 5)
            ax.set_ylim(-5, 5)
            line, = ax.plot(0, 0)

            # Create array of vectors
            vectors = [
                None] * int(input("Enter the number of vectors to be used in function estimations: "))

            step = 1 / 100
            for j in range(len(vectors)):
                n = findN(j)
                addedPoints = complex(0, 0)
                # Calculate average point
                for k in range(100):
                    t = k * step
                    actualValue = complex(
                        0.75*(2 * (1 + math.cos(t)) * math.sin(t)), -(2 * (1 + math.cos(t)) * math.cos(t)))
                    eTerm = (math.e**(-2*math.pi*i*n*t))
                    addedPoints += (eTerm * actualValue)
                averagePoint = addedPoints / 100
                vectors[j] = {"coefficient": averagePoint}

            def animation_frame(t):
                x_data.append(estimatePoint(vectors, t).real)
                y_data.append(-(estimatePoint(vectors, t).imag))

                line.set_data(x_data, y_data)
                return line,

            animation = FuncAnimation(fig, func=animation_frame,
                                      frames=np.arange(1, 100, 0.01), interval=10)
            plt.show()

    elif userInput == "Display UDWD":

        x_data = []
        y_data = []

        fig, ax = plt.subplots()
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        line, = ax.plot(0, 0)

        def animation_frame(i):
            x_data.append(math.sin(i)*math.cos(i)*math.log(abs(i)))
            y_data.append((abs(i)**0.3) * (math.cos(i)**(1/2)))

            line.set_data(x_data, y_data)
            return line,

        animation = FuncAnimation(fig, func=animation_frame,
                                  frames=np.arange(1, 100, 0.05), interval=10)
        plt.show()

    elif userInput == "Display I8":

        x_data = []
        y_data = []

        fig, ax = plt.subplots()
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        line, = ax.plot(0, 0)

        def animation_frame(i):
            x_data.append(math.sin(i)*math.cos(i)*math.log(abs(i)))
            y_data.append(2 * (1 + math.cos(i)) * math.sin(i))

            line.set_data(x_data, y_data)
            return line,

        animation = FuncAnimation(fig, func=animation_frame,
                                  frames=np.arange(1, 100, 0.05), interval=10)
        plt.show()

        # Initialize starting data
        x_data = []
        y_data = []
        samplePoints = int(input(
            "Enter the number of sample points to be taken for vector estimations: "))
        step = 1 / samplePoints
        numberOfVectors = int(
            input("Enter the number of vectors to be used in function estimations: "))
        fig, ax = plt.subplots()
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        line, = ax.plot(0, 0)
        i = complex(0, 1)

        # Calculate the coefficients of the vectors
        vectorCoefficients = [None] * numberOfVectors
        for temp in range(numberOfVectors):
            if temp == 0:
                n = 0
            elif temp % 2 == 0:
                n = int(-1 * (temp / 2))
            else:
                n = int((temp + 1) / 2)

            # Reset the x and y data
            totalX, totalY = 0, 0
            # Calculate the average of the sample points
            for j in range(samplePoints):
                t = (j * step) + 0.00000000001
                point = (math.e ** (-2*math.pi*i*n*t)) * (complex((math.sin(t) *
                                                                   math.cos(t)*math.log(abs(t))), (2 * (1 + math.cos(t)) * math.sin(t))))
                totalX += point.real
                totalY += point.imag
            averageX = (totalX / samplePoints).real
            averageY = (totalY / samplePoints).real

            vectorLength = math.sqrt(averageX**2 + averageY**2)

            if averageX > 0:
                radians = math.atan(averageY / averageX)
            elif averageX == 0:
                radians = math.pi / 2
            else:
                radians = math.atan(averageY / averageX) + math.pi

            vectorCoefficients[temp] = vectorLength * \
                (math.e**(complex(0, radians)))

        # Animation
        def animation_frame(t):
            finalPoint = complex(0, 0)

            for temp in range(numberOfVectors):
                if temp == 0:
                    n = 0
                elif temp % 2 == 0:
                    n = int(-1 * (temp / 2))
                else:
                    n = int((temp + 1) / 2)

                coefficient = vectorCoefficients[temp]
                finalPoint += (coefficient * (math.e**(n*2*math.pi*i*t)))

            x_data.append(finalPoint.real)
            y_data.append(finalPoint.imag)

            line.set_data(x_data, y_data)
            return line,

        animation = FuncAnimation(fig, func=animation_frame,
                                  frames=np.arange(1, 100, 0.01), interval=10)
        plt.show()

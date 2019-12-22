"""Numerical differentiation"""

import numpy as np


def derivative_backward_difference(x, y):
    """
    Calculate the first derivative
    All values in 'x' must be equally spaced
    Parameters:
            x: Array containing x values
            y: Array containing y values
    Returns:
           dy: Array containing the first derivative values
    """

    if x.size < 2 or y.size < 2:
        raise "Error: 'x' and 'y' arrays must have 2 values or more."

    if x.size != y.size:
        raise "Error: 'x' and 'y' must have same size."

    def dy_difference(h, y0, y1):
        return (y1 - y0) / h

    n = x.size
    dy = np.zeros(n)
    for i in range(0, n):
        if i == n - 1:
            h = x[i] - x[i - 1]
            dy[i] = dy_difference(-h, y[i], y[i - 1])
        else:
            h = x[i + 1] - x[i]
            dy[i] = dy_difference(h, y[i], y[i + 1])

    return [dy]


def derivative_three_point(x, y):
    """
    Calculate the first derivative
    All values in 'x' must be equally spaced
    Parameters:
            x: Array containing x values
            y: Array containing y values
    Returns:
           dy: Array containing the first derivative values
    """

    if x.size < 3 or y.size < 3:
        raise "Error: 'x' and 'y' arrays must have 3 values or more."

    if x.size != y.size:
        raise "Error: 'x' and 'y' must have same size."

    def dy_mid(h, y0, y2):
        return (1 / (2 * h)) * (y2 - y0)

    def dy_end(h, y0, y1, y2):
        return (1 / (2 * h)) * (-3 * y0 + 4 * y1 - y2)

    h = x[1] - x[0]
    n = x.size
    dy = np.zeros(n)
    for i in range(0, n):
        if i == 0:
            dy[i] = dy_end(h, y[i], y[i + 1], y[i + 2])
        elif i == n - 1:
            dy[i] = dy_end(-h, y[i], y[i - 1], y[i - 2])
        else:
            dy[i] = dy_mid(h, y[i - 1], y[i + 1])

    return [dy]


def derivative_five_point(x, y):
    """
    Calculate the first derivative
    All values in 'x' must be equally spaced
    Parameters:
            x: Array containing x values
            y: Array containing y values
    Returns:
           dy: Array containing the first derivative values
    """

    if x.size < 6 or y.size < 6:
        raise "Error: 'x' and 'y' arrays must have 6 values or more."

    if x.size != y.size:
        raise "Error: 'x' and 'y' must have same size."

    def dy_mid(h, y0, y1, y3, y4):
        return (1 / (12 * h)) * (y0 - 8 * y1 + 8 * y3 - y4)

    def dy_end(h, y0, y1, y2, y3, y4):
        return (1 / (12 * h)) * \
               (-25 * y0 + 48 * y1 - 36 * y2 + 16 * y3 - 3 * y4)

    h = x[1] - x[0]
    n = x.size
    dy = np.zeros(n)
    for i in range(0, n):
        if i in (0, 1):
            dy[i] = dy_end(h, y[i], y[i + 1], y[i + 2], y[i + 3], y[i + 4])
        elif i in (n - 1, n - 2):
            dy[i] = dy_end(-h, y[i], y[i - 1], y[i - 2], y[i - 3], y[i - 4])
        else:
            dy[i] = dy_mid(h, y[i - 2], y[i - 1], y[i + 1], y[i + 2])

    return [dy]

import math


def bisection(f, a, b, tol, iter_max):
    """
    Calculates the root of an equation by Bisection method
    Inputs:
            f: Function f(x)
            a: Lower limit
            b: Upper limit
          tol: Tolerance
     iter_max: Maximum number of iterations
    Outpus:
         root: Root value
         iter: Used iterations
    converged: Found the root
    """

    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        raise "Error: The function does not change signal at \
              the ends of the given interval."

    delta_x = math.fabs(b - a) / 2

    x = 0
    converged = False
    i = 0
    for i in range(0, iter_max + 1):
        x = (a + b) / 2
        fx = f(x)

        print("i: {:03d}\t x: {:+.4f}\t fx: {:+.4f}\t dx: {:+.4f}\n"
              .format(i, x, fx, delta_x), end="")

        if delta_x <= tol and math.fabs(fx) <= tol:
            converged = True
            break

        if fa * fx > 0:
            a = x
            fa = fx
        else:
            b = x

        delta_x = delta_x / 2
    else:
        print("Warning: The method did not converge.")

    root = x
    return [root, i, converged]


def newton(f, df, x0, tol, iter_max):
    """
    Calculates the root of an equation by Newton method
    Inputs:
            f: Function f(x)
           df: Derivative of function f(x)
           x0: Initial guess
          tol: Tolerance
     iter_max: Maximum number of iterations
    Outpus:
         root: Root value
         iter: Used iterations
    converged: Found the root
    """

    x = x0
    fx = f(x)
    dfx = df(x)

    converged = False
    print("iter: 0 x: {:.4f}\t dfx: {:.4f}\t fx: {:.4f}\n"
          .format(x, dfx, fx), end="")

    i = 0
    for i in range(1, iter_max + 1):
        delta_x = -fx / dfx
        x += delta_x
        fx = f(x)
        dfx = df(x)

        print("i:{:03d}\t x: {:.4f}\t dfx: {:.4f}\t fx: {:.4f}\t dx: {:.4f}\n"
              .format(i, x, dfx, fx, delta_x), end="")

        if math.fabs(delta_x) <= tol and math.fabs(fx) <= tol or dfx == 0:
            converged = True
            break
    else:
        print("Warning: The method did not converge.")

    root = x
    return [root, i, converged]


def secant(f, a, b, tol, iter_max):
    """
    Calculates the root of an equation by Secant method
    Inputs:
            f: Function f(x)
            a: Lower limit
            b: Upper limit
          tol: Tolerance
     iter_max: Maximum number of iterations
    Outpus:
         root: Root value
         iter: Used iterations
    converged: Found the root
    """

    fa = f(a)
    fb = f(b)

    if fb - fa == 0:
        raise "Error: f(b)-f(a) must be nonzero."

    if b - a == 0:
        raise "Error: b-a must be nonzero."

    if math.fabs(fa) < math.fabs(fb):
        a, b = b, a
        fa, fb = fb, fa

    x = b
    fx = fb

    converged = False
    i = 0
    for i in range(0, iter_max + 1):
        delta_x = -fx / (fb - fa) * (b - a)
        x += delta_x
        fx = f(x)

        print("i: {:03d}\t x: {:+.4f}\t fx: {:+.4f}\t dx: {:+.4f}\n"
              .format(i, x, fx, delta_x), end="")

        if math.fabs(delta_x) <= tol and math.fabs(fx) <= tol:
            converged = True
            break

        a, b = b, x
        fa, fb = fb, fx
    else:
        print("Warning: The method did not converge.")

    root = x
    return [root, i, converged]

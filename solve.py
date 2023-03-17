import time

def f(x):
    return x**5 + x**3 - 2*x - 5

def bisection(a, b, tol=1e-6, max_iterations=100):
    """
    This function implements the bisection method to solve the nonlinear equation f(x) = 0.
    a: left endpoint of the initial interval
    b: right endpoint of the initial interval
    tol: tolerance for convergence
    max_iterations: maximum number of iterations to perform
    """
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        return None
    for i in range(max_iterations):
        c = (a + b) / 2
        fc = f(c)
        if abs(fc) < tol:
            return c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return None

def newton_raphson(x0, tol=1e-6, max_iterations=100):
    """
    This function implements the Newton-Raphson method to solve the nonlinear equation f(x) = 0.
    x0: initial guess
    tol: tolerance for convergence
    max_iterations: maximum number of iterations to perform
    """
    x = x0
    for i in range(max_iterations):
        fx = f(x)
        dfx = 5*x**4 + 3*x**2 - 2
        if abs(fx) < tol:
            return x
        x = x - fx / dfx
    return None

x0 = 2.0
start_time = time.time()
root = newton_raphson(x0)
elapsed_time = time.time() - start_time
if root is not None:
    print("The root found by Newton-Raphson is:", root)
    print("Time taken by Newton-Raphson:", elapsed_time, "seconds")
else:
    print("Newton-Raphson failed to converge.")

a = 0.0
b = 3.0
start_time = time.time()
root = bisection(a, b)
elapsed_time = time.time() - start_time
if root is not None:
    print("The root found by bisection is:", root)
    print("Time taken by bisection:", elapsed_time, "seconds")
else:
    print("Bisection failed to converge.")

import time

def f(x):
    return x**5 + x**3 - 2*x - 5

def df(x):
    return 5*x**4 + 3*x**2 - 2

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
        dfx = df(x)
        if abs(fx) < tol:
            return x
        x = x - fx / dfx
    return None

x0 = 2.0
start_time = time.time()
root = newton_raphson(x0)
elapsed_time = time.time() - start_time
if root is not None:
    print("The root is:", root)
    print("Time taken:", elapsed_time, "seconds")
else:
    print("Failed to converge.")
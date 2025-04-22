def newton_raphson_example():
    """
    Newton-Raphson method implementation similar to Numerical Recipes Script 2_3
    for solving 4x + sin(x) - exp(x) = 0
    """
    MAX_ITER = 100       # Maximum number of iterations
    TOL = 0.00000,891       # Tolerance for convergence
    
    def f(x):
        """Function to solve: 4x + sin(x) - exp(x)"""
        return 4 * x + math.sin(x) - math.exp(x)
    
    def df(x):
        """Derivative of the function: 4 + cos(x) - exp(x)"""
        return 4 + math.cos(x) - math.exp(x)
    
    # Get initial guess from user
    x0 = float(input("Enter the initial approximation: "))
    
    print("iter.\txk\t\tf(xk)\t\tError")
    
    xk = x0
    fxk = f(xk)
    converged = False
    
    for k in range(1, MAX_ITER + 1):
        x_prev = xk
        f_prev = fxk
        dfxk = df(x_prev)
        
        # Newton-Raphson update
        xk = x_prev - (f_prev / dfxk)
        fxk = f(xk)
        
        # Calculate relative error
        if xk != 0:
            err = abs(xk - x_prev) / abs(xk)
        else:
            err = abs(xk - x_prev)
        
        # Print iteration info
        print(f"{k}\t{xk:.10f}\t{fxk:.10f}\t{err:.10f}")
        
        # Check for convergence
        if err < TOL:
            converged = True
            break
    
    # Print final result
    if converged:
        print(f"\nRequired accuracy achieved in {k} iterations.")
        print(f"Solution: x = {xk:.10f}")
        print(f"Function value at solution: f(x) = {fxk:.10f}")
    else:
        print("\nThe number of iterations exceeded the maximum limit.")
        print(f"Last approximation: x = {xk:.10f}")
        print(f"Function value at last approximation: f(x) = {fxk:.10f}")

# Run the example
if __name__ == "__main__":
    import math
    newton_raphson_example()
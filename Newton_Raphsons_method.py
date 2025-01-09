"""
Solve the equation f(x)=x^2 - 4 using the Newton-Raphson method. Start with an initial guess x0 =3. Perform 3 iterations
"""
def f(x):
    return x**2 - 4

def first_derivative_f(x):
    return 2*x

def newton_raphson(f, first_derivative_f, x0, itr):
    x = x0
    for i in range(itr):
        fx = f(x)                   # given function
        fdx = first_derivative_f(x)    # first derivative

        # calculating root (x) using newton raphson 
        x_new = x - fx / fdx
        print(f"iter-{i}: x = {x},  f(x)={fx}")
        x = x_new
    return x
        
x0 = 3
iteration = 3

result = newton_raphson(f,first_derivative_f, x0, iteration)
print(f"Approximate root(x) = {result}")

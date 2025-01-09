"""
Approximate the integral of f(x)=x^2 over the interval [0,1] using the trapezoidal rule with 2 subintervals
"""
# defining the given function
def f(x):
    return x**2

# a function to calculate the approzimate value using trapezoidal rule
def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    lst = []
    f1 = f(a)
    f2 = f(b)
    sum = f1 + f2
    print(f"The point lies between {f1} and {f2}")
    for i in range(1, n):
        val = a + i*h
        sum += 2 * f(val)
    return sum * (h / 2)

# initializing the values
first_limit = 0
last_limit = 1
subintervals = 2

# calling a function 
result = trapezoidal_rule(first_limit, last_limit, subintervals)

# printing the result
print(f"Approximate result = {result}")
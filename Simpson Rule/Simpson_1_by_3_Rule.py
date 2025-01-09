"""
Use Simpson's 1/3 rule to approximate the integral of f(x)=x^3 over the interval [0, 1] using 4 subintervals.
"""

def f(x):
    return x**3

def simpson_1_by_3_Rule(a, b, n):
    h = (b - a) / n

    sum = f(a) + f(b)

    for i in range(1, n):
        val = a + i*h
        if i % 2 == 0:
            sum += 2*f(val)
        else:
            sum += 4*f(val)
    return sum* (h/3)

first_limit = 0
last_limit = 1
subintervals = 4

result = simpson_1_by_3_Rule(first_limit, last_limit, subintervals)
print(f"Approximate result = {result}")
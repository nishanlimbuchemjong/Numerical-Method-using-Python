"""
Find Solution of an equation 1/x using Simpson's 3/8 rule
    x1 = 1 and x2 = 2
"""
# defining the function
def f(x):
    return 1/x

# a function for calculating the appropriate value using simpson 3/8 rule
def simpson_3_by_8_Rule(a, b, n):
    h = (b - a) / n
    sum = f(a) + f(b)

    for i in range(1, n):
        val = a + i * h
        if i % 3 == 0:
            sum += 2 * f(val)
        else:
            sum += 3 * f(val)

    return (3*h/8) * sum

# initializing the values
first_limit = 1 
last_limit = 2
iteration = 4

# calling out the function 
result = simpson_3_by_8_Rule(first_limit, last_limit, iteration)

# printing out the result
print(f"Approximate result = {result}")

#  output: Approximate result = 0.7138392857142858
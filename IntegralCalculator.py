def string_to_function(expression):
    def function(x):
        return eval(expression)

    return function


def simpson_aprox(function, n, a, b):
    a = int(a)
    b = int(b)
    n = int(n)
    w = (b - a) / n * 1.0
    ##odd sum
    i = a + w
    odds = 0
    while i < b:
        odds = odds + function(i)
        i = i + 2 * w

    ##even sum
    i = a + 2 * w
    evens = 0
    while i < b:
        evens = evens + function(i)
        i = i + 2 * w

    ##total sum
    total = (w / 3.0) * (function(a) + 4 * odds + 2 * evens + function(b))

    return total


print("Enter function")
my_function = string_to_function(input())
print("Enter end-point 1")
f = input()
print("Enter end-point 2")
l = input()
print("Enter accuracy (number of measurements)")
boxes = input()
aprox = simpson_aprox(my_function, boxes, f, l)
print("Integral = ", aprox)
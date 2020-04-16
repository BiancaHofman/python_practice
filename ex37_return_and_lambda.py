#1. Normal function that returns the result 36
#And this result is printed
def name():
    a = 6
    return a * 6
    
print(name())


#2. Normal function that only prints the result 36
def name():
    a = 6
    
    print(a * 6)

name()

#3. Anonymous function that returns the result 36
#And this result is printed
x = lambda a: a * 6
print(x(6))


#4. Normal function that returns the result 30
#And this result is printed
def multiply():
    a = 6
    b = 5
    return a * b
print(multiply())


#5. Normal function that only prints the result 30
def multiply():
    a = 6
    b = 5
    
    print(a * b)

multiply()

#6.Anonymous function that returns result 30
#And this result is prints
multiply = lambda a, b: a * b
print(multiply (6,5))
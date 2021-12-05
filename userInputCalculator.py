import numpy as np
import sys

twoInputfunctions = ['add','subtract','multiply','divide']
oneInputfunctions = ['ln','square root', 'sine', 'cosine','sin','cos']
total = None

def add(a,b): return a + b

def subtract(a,b): return a - b

def multiply(a,b): return a * b

def divide(a,b): return a / b

def log(a): return np.log(a)

def squareRoot(a): return np.sqrt(a)

def sine(a): return np.sin(a)

def cosine(a): return np.cos(a)

print("This is a calculator:", sys.argv[0])
while True:
    input = input("Choose an operation: add,subtract,multiply,divide,ln,square root,sine,cosine,sin,cos \n")
    if input in twoInputfunctions:
        num1 = float(input("Gimme the first number: "))
        num2 = float(input("Gimme the second number: "))
        if input == 'add':
            total = add(num1,num2)
        elif input == 'subtract':
            total = subtract(num1,num2)
        elif input == 'multiply':
            total = multiply(num1,num2)
        elif input == 'divide':
            total = divide(num1,num2)
    if input in oneInputfunctions:
        num = float(input("Gimme the number: "))
        if input == 'ln':
            total = log(num)
        elif input == 'squareRoot':
            total = squareRoot(num)
        elif input == 'sin' or input == 'sine':
            total = sine(num)
        elif input == 'cos' or input == 'cosine':
            total = cosine(num)
    print("Your total is %d" % (total))

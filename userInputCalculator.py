import numpy as np
import sys

twoInputfunctions = ['add','subtract','multiply','divide']
oneInputfunctions = ['ln','square root', 'sine', 'cosine','sin','cos']
total : float

def add(a,b): return float(a + b)

def subtract(a,b): return float(a - b)

def multiply(a,b): return float(a * b)

def divide(a,b): return float(a / b)

def log(a): return np.log(a)

def squareRoot(a): return np.sqrt(a)

def sine(a): return np.sin(a)

def cosine(a): return np.cos(a)

print("This is a calculator:", sys.argv[0])
while True:
    func = input("Choose an operation: add,subtract,multiply,divide,ln,square root,sine,cosine,sin,cos \n")
    if func in twoInputfunctions:
        num1 = float(input("Gimme the first number: "))
        num2 = float(input("Gimme the second number: "))
        if func == 'add':
            total = add(num1,num2)
        elif func == 'subtract':
            total = subtract(num1,num2)
        elif func == 'multiply':
            total = multiply(num1,num2)
        elif func == 'divide':
            total = divide(num1,num2)
    if func in oneInputfunctions:
        num = float(input("Gimme the number: "))
        if func == 'ln':
            total = log(num)
        elif func == 'squareRoot':
            total = squareRoot(num)
        elif func == 'sin' or func == 'sine':
            total = sine(num)
        elif func == 'cos' or func == 'cosine':
            total = cosine(num)
    print("Your total is %d" % (total))

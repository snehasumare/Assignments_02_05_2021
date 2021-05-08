# 1. Write a function and  call that function without using return keyword
def addition(x,y):
    z=x+y
    print("addition is:", z)

def substraction(x,y):
    z=x-y
    print("substraction is:", z)

def multiplication(x,y):
    z=x*y
    print("multiplication is:", z)

def division(x,y):
    if y==0:
        print("Division is not possible")
    return
    z=x/y
    print("division is:", z)

x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
addition(x,y)
substraction(x,y)
multiplication(x,y)
division(x,y)

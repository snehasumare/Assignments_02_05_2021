def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

result=factorial(8)
print(result)
#Write a program for Mathematical operations in a single function
def operation(a,b,o):
    if o=="A":
        return a+b
    if o=="S":
        return a-b
    if o=="M":
        return a*b
    if o=="D":
        if b!=0:
            return a/b
        else:
            return 0
p=int(input("Enter First no.:"))
q=int(input("Enter Second no.:"))
r=input("Enter A/S/M/D to perform operation:")
result = operation(p,q,r)
print(result)
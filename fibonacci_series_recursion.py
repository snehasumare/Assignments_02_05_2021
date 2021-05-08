def fibo(a,b):
    if(b>100):
        return
    c=a+b
    print(c)
    fibo(b,c)


print(0,"\n",1)
fibo(0,1)
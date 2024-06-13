def num(n):
    A=[]
    for i in range(1,n+1):
        if n % i ==0:
            A.append(i)
    return A        

n=20
print(num(n))

def isprime(n):
    for j in range(2, n // 2):
        if n % j == 0:
            return 0
    return n

n=int(input())
for i in range(2,1000):
    x=isprime(i)
    if x!=0:
        while n%x==0:
            print(x,end=" ")
            n=n//x
            if n==0:
                break


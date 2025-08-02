def prime(n):
    if n<2:
        return 0
    for i in range(2,n):
        if n%i == 0:
            return 0
    else:
        return 1

def arm(n):
    l = len(str(n))
    s = 0
    for i in str(n):
        s = s+int(i)**l
    if s==n:
        return 1
    else:
        return 0

n = int(input())
for i in range(1,n+1):
    if prime(i) == 1:
        if arm(i) == 1:
            print(i,end = " ")
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
c = 0
for i in range(1,n+1):
    if arm(i) == 1:
        c += 1
print(c)
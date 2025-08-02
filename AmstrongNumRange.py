def arm(n):
    l = len(str(n))
    s = 0
    for i in str(n):
        s = s+int(i)**l
    if n == s:
        return 1
    else:
        return 0




n = int(input())
for i in range(1,n+1):
    if arm(i) == 1:
        print(i,end=" ")
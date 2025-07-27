def arm(n):
    l = len(str(n))
    s=0
    for i in str(n):
        s = s + int(i)**l
    if s == n:
        return 1
    else:
        return 0




n = int(input())
if arm(n) == 1:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
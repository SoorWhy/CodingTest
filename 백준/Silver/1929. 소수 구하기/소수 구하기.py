a, b = map(int, input().split())

n = [True] * (b+1) # 0~16
n[0], n[1] = False, False

for i in range(2, int(b**0.5)+1):
    if n[i]:
        for j in range(i*i, b+1, i):
            n[j] = False

for i in range(a, b+1):
    if n[i]:
        print(i)
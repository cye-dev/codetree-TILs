import sys

n, m = map(int, sys.stdin.readline().split())
arr = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]
ans = 0

for row in range(n):
    num = 0
    cnt = 1
    
    for col in range(n):
        if num == arr[row][col]:
            cnt += 1
            if cnt >= m:
                ans += 1
                break
        else:
            num = arr[row][col]
            cnt = 1

for col in range(n):
    num = 0
    cnt = 1
    
    for row in range(n):
        if num == arr[row][col]:
            cnt += 1
            if cnt >= m:
                ans += 1
                break
        else:
            num = arr[row][col]
            cnt = 1

print(ans)
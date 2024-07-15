import sys

N = int(sys.stdin.readline())
arr = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(N)
]
ans = 0

for i in range(N):
    for j in range(N):
        if i + 2 >= N or j + 2 >= N:
            continue

        cnt = 0
        for m in range(i, i + 3):
            for n in range(j, j + 3):
                if arr[m][n] == 1:
                    cnt += 1

        if ans < cnt:
            ans = cnt

print(ans)
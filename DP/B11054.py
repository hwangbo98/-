import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

Lis = [1] * (N)
Lds = [1] * (N)

for i in range(N) :
    for j in range(i) :
        if A[i] > A[j] :
            Lis[i] = max(Lis[i], Lis[j] + 1)

for i in range(N-1, -1, -1) :
    for j in range(N-1, i, -1) :
        if A[i] > A[j] :
            Lds[i] = max(Lds[i], Lds[j] + 1)

# print(max(Lis) + max(Lds) - 1)
# print(Lis, Lds)

max_length = 0

for k in range(N) :
    max_length = max(max_length, Lis[k] + Lds[k] -1)

print(max_length)

import sys

input = sys.stdin.readline

N = int(input())

dp = [[0] * 10 for _ in range((N+1))]

for i in range(10) :
    dp[1][i] = 1
# print(dp)

for k in range(2,N+1) :
    for j in range(10) :
        if j == 0 :
            dp[k][j] = dp[k-1][j]
        else :
            dp[k][j] = dp[k][j-1] + dp[k-1][j]

result = sum(dp[N]) % 10007
print(result)

import sys

input = sys.stdin.readline

n = int(input())
dp = [-1] * (n + 1)

# 초기값 설정
if n >= 3:
    dp[3] = 1
if n >= 5:
    dp[5] = 1

# DP 테이블 채우기
for i in range(6, n + 1):
    # 이전 3kg 또는 5kg을 사용할 수 있는 경우 갱신
    if dp[i - 3] != -1:
        dp[i] = dp[i - 3] + 1
    if dp[i - 5] != -1:
        if dp[i] == -1:
            dp[i] = dp[i - 5] + 1
        else:
            dp[i] = min(dp[i], dp[i - 5] + 1)

# 결과 출력
print(dp[n])
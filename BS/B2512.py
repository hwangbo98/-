import sys

N = int(input())

jibang = list(map(int, input().split()))
budget = int(input())

left = 0
right = max(jibang)
answer = -1
count = 0
while left <= right :
    middle = (left + right) // 2

    sum = 0
    count+=1
    for i in range(N) :
        sum += min(middle, jibang[i])

    if sum <= budget :
        answer = middle
        left = middle + 1
    else :
        right = middle - 1

print(answer)
# print(count)
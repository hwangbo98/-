import sys

input = sys.stdin.readline

gear = list(map(int, input().split()))

sum = 0
cond = True
for i in range(len(gear) - 1) :
    if abs(gear[i+1] - gear[i]) > 1 :
        print('mixed')
        cond = False
        break
    else :
        sum += (gear[i+1] - gear[i])

if cond and sum == 7 :
    print('ascending')
elif cond and sum == -7 :
    print('descending')


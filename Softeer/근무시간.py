import sys

input = sys.stdin.readline

total = 0
for _ in range(5) :
    work, home = map(str, input().split())
    w_h, w_m = map(int, work.split(':'))
    h_h, h_m = map(int, home.split(':'))

    total_work = w_h * 60 + w_m
    total_home = h_h * 60 + h_m

    total +=(total_home - total_work)

print(total)

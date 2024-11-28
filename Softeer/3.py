import sys

input = sys.stdin.readline

W, N = map(int, input().split())

info = []
for _ in range(N) :
    M, P = map(int, input().split())
    info.append((M, P))

print(info)

sorted_info = sorted(info, key = lambda x : x[1], reverse=True )

print(sorted_info)
cost = 0
for m, p in sorted_info :
    if m > W :
        print(f'W : {W}')
        cost += W*p
        W -= W

    else :
        W-=m
        cost += m*p

print(cost)
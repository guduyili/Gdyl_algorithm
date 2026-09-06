import sys

input = sys.stdin.readline

n, m, q = map(int, input().split())

# 一定要把两个边界放进去
cut_n = {0, n}
cut_m = {0, m}

for _ in range(q):
    opt, x = map(int, input().split())

    if opt == 0:
        cut_n.add(x)
    else:
        cut_m.add(x)

cut_n = sorted(cut_n)
cut_m = sorted(cut_m)

# 长度方向最小间隔
min_n = n
for i in range(1, len(cut_n)):
    min_n = min(min_n, cut_n[i] - cut_n[i - 1])

# 宽度方向最小间隔
min_m = m
for i in range(1, len(cut_m)):
    min_m = min(min_m, cut_m[i] - cut_m[i - 1])

print(min_n * min_m)
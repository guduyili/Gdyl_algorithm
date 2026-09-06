n = int(input())

L = len(str(n))

# 所有位数 < L 的答案
ans = 9 * (L - 1) * (L - 2) // 2

# 只枚举 L 位数
for d in range(1, 10):
    for zero_pos in range(1, L):
        s = [str(d)] * L
        s[zero_pos] = '0'

        x = int(''.join(s))

        if x <= n:
            ans += 1

print(ans)
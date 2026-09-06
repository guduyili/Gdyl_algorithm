


import sys

# 第 i 种食物需要连续吃 a[i] 天，每天吃 b[i] 份。
def main():
    input = sys.stdin.readline

    n, k = map(int, input().split())

    foods = []
    total = 0

    for _ in range(n):
        a, b = map(int, input().split())
        foods.append((a, b))
        total += b

    # 第一天就满足
    if total <= k:
        print(1)
        sys.exit()


    # 按吃完的时间顺序排序
    foods.sort()

    i = 0
    while i < n:
        day = foods[i][0]

        # 所有在 day天吃完的食物一起删除
        while i < n and foods[i][0] == day:
            total -= foods[i][1]
            i += 1
        # 删除后对应的是第 day + 1 天
        if total <= k:
            print(day+1)
            break


if __name__ == "__main__":
    main()
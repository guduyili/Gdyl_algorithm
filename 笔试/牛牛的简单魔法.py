## << 左移
## >> 右移

# # 判断第i个数字为0 或 1
# # a_mask, b_mask 初始为0
# # <<  1的数字位左移动
# # >>  1的数字位右移动 
# # 移动到 i 位 判断是否为 0（既为没有被使用过）
# # 0>>0 = 0
# # i = 0,1>>0 = 1 = 0001
# # i = 2,1>>1 = 0 = 0000
# if not ((b_mask>>i) & 1):
#     # 标记已经使用过的第i位
#     # i = 0,1<<0 = 1 = 0001,0|1 = 1 = 0001
#     # i = 1,1<<1 = 2 = 0010,1|2 = 3 = 0011 
#     b_mask | (1<<i)
import sys
import math
sys.setrecursionlimit(10000)

    
# # 判断b数组在m大小限制中是否有剩余为1的
# (b_mask != (1<<m)-1)

# 当前血量 hp

# 增幅水晶使用情况 a_mask

# 单体伤害法术使用情况 b_mask

# 魔法三是否使用 used3

# 魔法四是否使用 used4

# 上一步是否使用了增幅水晶，若使用了，则存下倍率 last_amp
def can_win(hp, a_mask, b_mask, used3, used4, last_amp, n, m, p, q, a, b):
    """深度优先搜索，判断是否能击败怪物"""
    if hp < 1:
        return True

    # 上一步使用了增幅，当前必须释放伤害魔法
    if last_amp > 0:
        # 魔法二：单体伤害
        for i in range(m):
            if not ((b_mask >> i) & 1):
                damage = last_amp * b[i]
                if can_win(hp - damage, a_mask, b_mask | (1 << i), used3, used4, 0, n, m, p, q, a, b):
                    return True
        # 魔法三：百分比伤害
        if not used3:
            damage = last_amp * ((p * hp) // q)
            if can_win(hp - damage, a_mask, b_mask, True, used4, 0, n, m, p, q, a, b):
                return True
        # 魔法四：开方伤害
        if not used4:
            damage = last_amp * int(math.isqrt(hp))
            if can_win(hp - damage, a_mask, b_mask, used3, True, 0, n, m, p, q, a, b):
                return True
        return False

    # 上一步未使用增幅，可以自由选择
    # 先检查是否还有可用的伤害魔法（用于决定是否值得使用增幅）
    has_damage = (b_mask != (1 << m) - 1) or (not used3) or (not used4)

    # 选择使用魔法一（增幅）
    if has_damage:
        for i in range(n):
            if not ((a_mask >> i) & 1):
                if can_win(hp, a_mask | (1 << i), b_mask, used3, used4, a[i], n, m, p, q, a, b):
                    return True

    # 不使用增幅，直接使用魔法二
    for i in range(m):
        if not ((b_mask >> i) & 1):
            if can_win(hp - b[i], a_mask, b_mask | (1 << i), used3, used4, 0, n, m, p, q, a, b):
                return True

    # 不使用增幅，直接使用魔法三
    if not used3:
        damage = (p * hp) // q
        if can_win(hp - damage, a_mask, b_mask, True, used4, 0, n, m, p, q, a, b):
            return True

    # 不使用增幅，直接使用魔法四
    if not used4:
        damage = int(math.isqrt(hp))
        if can_win(hp - damage, a_mask, b_mask, used3, True, 0, n, m, p, q, a, b):
            return True

    return False


def solve():
    # input_data = sys.stdin.readline
    # print("input:",input_data)
    input = sys.stdin.readline
    T = int(input())
    results = []

    for _ in range(T):
        n, m, p, q, y = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        hp = 10 ** 9 + y  # 初始血量（题目中 x = 10^9，输入给出 y）
        if can_win(hp, 0, 0, False, False, 0, n, m, p, q, a, b):
            results.append("YES")
        else:
            results.append("NO")

    sys.stdout.write("\n".join(results))

    # input = sys.stdin.readline
    # T = int(input())
    # ret = []

    # for _ in range(T):
    #     # 读取一行，按空格分割，映射为 5 个整数，分别赋给 n, m, p, q, y
    #     n,m,p,q,y = map(int,input().split())
    #     # 读取下一行，分割后转为整数列表，赋值给 a（通常长度应为 n）
    #     a=list(map(int,input().split()))
    #     b=list(map(int,input().split()))



if __name__ == "__main__":
    solve()
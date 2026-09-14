# 仓库可以表示为一个 n × m 的网格，有 k 个机器人在仓库中协同搬运货物。

# 每个机器人具有四个属性：

# 位置：(x, y)
# 方向：N / E / S / W
# 搬运状态：0 / 1

# 其中：

# 0：没有搬运货物
# 1：正在搬运货物

# 系统会进行 t 轮操作。

# 每一轮，每个机器人都会收到一条指令。

# 指令共有五种：

# F：向当前方向前进一格
# L：向左旋转 90°
# R：向右旋转 90°
# P：拿起货物，将搬运状态设为 1
# Q：放下货物，将搬运状态设为 0

# 所有机器人在一轮中的操作同时发生。


# n：网格行数
# m：网格列数
# k：机器人数量
# t：操作轮数

# 接下来 k 行：

# x y d carry

# 3 5 4 3
# 2 2 E 0
# 2 3 E 1
# 2 4 E 0
# 2 5 E 1
# FFFF
# LRPQ
# FFFF
import sys
from collections import deque

input = sys.stdin.readline


def solve():
    n, m, k, t = map(int, input().split())

    # 顺时针：N E S W
    dirs = "NESW"

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # robot[i] = [x, y, direction_index, carry]
    robots = []

    for _ in range(k):
        x, y, d, carry = input().split()

        d = dirs.index(d)
        carry = int(carry)

        robots.append([int(x), int(y), d, carry])

    # ==============================
    # 开始模拟 t 轮
    # ==============================

    for _ in range(t):

        commands = input().strip()

        # ---------------------------------
        # 记录本轮开始之前的位置
        # ---------------------------------

        old_pos = []

        position_to_robot = {}

        for i in range(k):
            x, y, d, carry = robots[i]

            old_pos.append((x, y))

            position_to_robot[(x, y)] = i

        # ---------------------------------
        # moving[i]
        # 表示机器人 i 本轮是否执行 F
        # ---------------------------------

        moving = [False] * k

        # target[i]
        # 表示机器人 i 想去的位置
        target = old_pos[:]

        # failed[i]
        # 表示机器人移动失败
        failed = [False] * k

        # ==============================
        # 第一步：
        # 计算所有机器人的行动意图
        # ==============================

        for i in range(k):

            cmd = commands[i]

            x, y, d, carry = robots[i]

            # --------------------------
            # 左转
            # --------------------------

            if cmd == 'L':

                # N -> W
                # W -> S
                # S -> E
                # E -> N

                robots[i][2] = (d - 1) % 4

            # --------------------------
            # 右转
            # --------------------------

            elif cmd == 'R':

                robots[i][2] = (d + 1) % 4

            # --------------------------
            # 拿起货物
            # --------------------------

            elif cmd == 'P':

                robots[i][3] = 1

            # --------------------------
            # 放下货物
            # --------------------------

            elif cmd == 'Q':

                robots[i][3] = 0

            # --------------------------
            # 前进
            # --------------------------

            elif cmd == 'F':

                moving[i] = True

                nx = x + dx[d]
                ny = y + dy[d]

                target[i] = (nx, ny)

                # 越界
                if not (1 <= nx <= n and 1 <= ny <= m):
                    failed[i] = True

        # ==============================
        # 第二步：
        # 判断多个机器人是否抢同一个格子
        # ==============================

        target_count = {}

        for i in range(k):

            # 必须是移动机器人
            # 而且不能已经越界
            if moving[i] and not failed[i]:

                pos = target[i]

                target_count[pos] = (
                    target_count.get(pos, 0) + 1
                )

        for i in range(k):

            if moving[i] and not failed[i]:

                if target_count[target[i]] >= 2:
                    failed[i] = True

        # ==============================
        # 第三步：
        # 判断两机器人交换位置
        # ==============================

        for i in range(k):

            if not moving[i]:
                continue

            # i 想去的位置
            pos = target[i]

            # pos 当前有没有机器人
            if pos not in position_to_robot:
                continue

            j = position_to_robot[pos]

            # j 也必须移动
            if not moving[j]:
                continue

            # 判断：
            #
            # i -> j原位置
            # j -> i原位置
            #
            # 即交换位置

            if target[j] == old_pos[i]:

                failed[i] = True
                failed[j] = True

        # ==============================
        # 第四步：
        # 构造移动依赖关系
        #
        # reverse[j] 中保存：
        # 哪些机器人依赖 j 离开
        # ==============================

        reverse = [[] for _ in range(k)]

        for i in range(k):

            if not moving[i]:
                continue

            # 越界目标就不需要再处理了
            nx, ny = target[i]

            if not (1 <= nx <= n and 1 <= ny <= m):
                continue

            pos = target[i]

            # 目标本来就是空的
            if pos not in position_to_robot:
                continue

            # 目标位置原来有机器人 j
            j = position_to_robot[pos]

            # --------------------------
            # j 本轮不移动
            #
            # 那么 i 肯定不能进入
            # --------------------------

            if not moving[j]:

                failed[i] = True

            else:

                # i依赖j
                #
                # 如果j失败
                # i也必须失败

                reverse[j].append(i)

        # ==============================
        # 第五步：
        # BFS传播失败
        # ==============================

        q = deque()

        for i in range(k):

            if moving[i] and failed[i]:
                q.append(i)

        while q:

            u = q.popleft()

            # v依赖u成功离开
            for v in reverse[u]:

                if not failed[v]:

                    failed[v] = True

                    q.append(v)

        # ==============================
        # 第六步：
        # 同时更新所有成功移动的机器人
        # ==============================

        for i in range(k):

            if moving[i] and not failed[i]:

                robots[i][0] = target[i][0]
                robots[i][1] = target[i][1]

    # ==============================
    # 输出最终状态
    # ==============================

    for x, y, d, carry in robots:

        print(
            x,
            y,
            dirs[d],
            carry
        )


if __name__ == "__main__":
    solve()
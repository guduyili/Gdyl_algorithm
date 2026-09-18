class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        m,n = len(num1),len(num2)
        ret = [0] * (m+n)
        for i in range(m-1,-1,-1):
            x = ord(num1[i]) - ord('0')
            # 每一个位数记录一个total
            total = 0
            for j in range(n-1,-1,-1):
                y = ord(num2[j]) - ord('0')
                # 加上上次乘算的ret[i+j+1]
                total = x * y + ret[i+j+1]

                ret[i+j+1] = total %10
                # 进位是+=,防止覆盖
                ret[i+j] += total // 10
        # 如果首位是0，则从第二为开始切
        start = 1 if ret[0] == 0 else 0

        return ''.join(str(x) for x in ret[start:])


if __name__ == "__main__":
    solution = Solution()
    num1 = "123"
    num2 = "456"
    result = solution.multiply(num1, num2)
    print(f"Product of {num1} and {num2}: {result}")
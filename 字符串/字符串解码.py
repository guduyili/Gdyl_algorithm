class Solution:
    def decodeString(self, s: str) -> str:
        stack,ret,multi = [],"",0

        for c in s:
            # 遇到 [
            if c == '[':
                # 将之前的数字和ret字母存入stack
                stack.append([multi,ret])
                # 同时更新 ret
                ret,multi = "",0
            # 遇到 ]
            elif c == ']':
                #弹出之前的cur_multi,last_str
                cur_multi,last_str = stack.pop()
                ret = last_str + cur_multi * ret
            # 遇到 数字
            elif '0'<= c <= '9':
                # 如有连续数字则进位
                multi = multi * 10 + int(c)
            # 遇到 字母
            else:
                ret += c
        return ret

if __name__ == "__main__":
    solution = Solution()
    s = "3[a]2[bc]"
    result = solution.decodeString(s)
    s1 = "2[abc]3[cd]ef"
    result1 = solution.decodeString(s1)
    print(f"Decoded string for '{s}': {result}")
    print(f"Decoded string for '{s1}': {result1}")
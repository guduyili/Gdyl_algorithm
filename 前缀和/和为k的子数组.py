from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sorted(nums)
        ret = 0

        dp = [0] * (len(nums)+1)
        # 记录前缀和
        for i,num in enumerate(nums):
            dp[i+1] = dp[i] + num

        record = defaultdict(int)
        
        # dp[j] - dp[i] = k
        # dp[i] = dp[j] -k
        for dpj in dp:
            # dpi = dpj - k
            ret += record[dpj-k]

            # 记录当前的dpj += 1
            # 充当后期的dpi
            record[dpj] += 1
        return ret

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1]
    k = 2
    result = solution.subarraySum(nums, k)
    print(f"Number of subarrays that sum to {k}: {result}")
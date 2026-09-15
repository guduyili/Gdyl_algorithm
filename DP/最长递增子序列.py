from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ret = 0
        if not nums:
            return 0
        # dp[i] = max(dp[i],dp[j]+1)
        # 1 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                # j < i
                if nums[j] < nums[i]:
                    # 记录dp[i]的最大值 从nums[j] < nums[i]
                    # 得出至少dp[i] >= dp[j]+1
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
    print(s.lengthOfLIS([0,1,0,3,2,3]))
    print(s.lengthOfLIS([7,7,7,7,7,7,7]))
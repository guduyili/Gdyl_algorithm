class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left,right = 0,len(nums)-1
        while left < right:
            mid = left + (right-left) //2
            # 左侧小于 处于爬坡阶段
            if nums[mid] < nums[mid+1]:
                left = mid +1
            # 左侧大于，处于下坡阶段
            else:
                right = mid

        return left

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 1]
    peak_index = solution.findPeakElement(nums)
    print(f"Peak element index: {peak_index}, Peak element value: {nums[peak_index]}")
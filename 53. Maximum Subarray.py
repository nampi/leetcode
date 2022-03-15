def maxSubArray(self, nums: list[int]) -> int:
    maxSum = nums[0]
    curSum = nums[0]
    j = 1
    while j < len(nums):  # вроде можно по nums[1:] итерироваться
        curSum = max(curSum + nums[j], nums[j])
        maxSum = max(maxSum, curSum)
        j += 1

    return maxSum

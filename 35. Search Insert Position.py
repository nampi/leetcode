def searchInsert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        midpoint = (left + right) // 2
        val = nums[midpoint]
        if val == target:
            return midpoint
        elif val > target:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return left

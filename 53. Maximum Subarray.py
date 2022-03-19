def max_sub_array(nums: list[int]) -> int:
    max_sum = cur_sum = nums[0]
    for x in nums[1:]:
        cur_sum = max(cur_sum + x, x)
        max_sum = max(max_sum, cur_sum)

    return max_sum

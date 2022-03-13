def removeDuplicates(nums: list[int]) -> int:
    prev = nums[0]
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != prev:
            nums[k] = nums[i]
            prev = nums[k]
            k += 1
    return k
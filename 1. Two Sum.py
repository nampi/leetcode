def two_sum(nums: list[int], target: int) -> list[int]:
    mapping = {}
    for index, x in enumerate(nums):
        if x in mapping:
            return mapping[x], index
        mapping[target - x] = index


global_nums = [3, 1, 6, 4, 0]
global_target = 5
print(two_sum(global_nums, global_target))

def twoSum(nums: [], target: int) -> []:  # why do we need List[int]
    dict = {}
    for index, x in enumerate(nums):
        if x in dict:
            return dict[x], index # do we need to return [dict[x], index]
        dict[target - x] = index


nums = [3, 1, 6, 4, 0]
target = 5
print(twoSum(nums, target))
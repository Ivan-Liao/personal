nums = [2, 7, 11, 15]



"""
I feel like this is a kinda cool solution if nums never changes.  Constant time performance
"""
def two_sum(nums, target):
    solutions = {}
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            solutions[nums[i]+nums[j]] = [i, j]
    return solutions[target]

print(two_sum(nums,9))
print(two_sum(nums,26))
print(two_sum(nums,18))
print(two_sum(nums,17))
print(two_sum(nums,22))
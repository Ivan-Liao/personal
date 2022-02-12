def two_sum(nums, target):
    p1, p2 = 0, len(nums) - 1
    results = []
    while p1 < p2:
        if nums[p1] + nums[p2] > target:
            p2 -= 1
        elif nums[p1] + nums[p2] < target:
            p1 += 1
        else: 
            results.append([nums[p1], nums[p2]])
            p1 += 1
    return results
        
def three_sum(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    prev, cur = None, None 
    result_set = []
    for i, num in enumerate(nums):
        cur = num
        if prev == cur:
            continue
        else:
            two_sum_results = two_sum(nums[i+1:], -cur)
            for res in two_sum_results:
                result_set.append([cur, res[0], res[1]]) 
            prev = cur
    return result_set
        
        
if __name__ == "__main__":
    print(two_sum([1, 3, 5, 11], 16))
    print(three_sum([-1, 0, 1, 2, -1, -4]))
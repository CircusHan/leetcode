class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)) :
            k = target - nums[i]
            if k in d and d[k] != i :
                return [i, d[k]]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)) :
            v = target - nums[i]
            if v in d and d[v] != i :
                return [i, d[v]]
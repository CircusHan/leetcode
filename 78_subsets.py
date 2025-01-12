class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [nums]
        else:
            L1 = self.subsets(nums[:-1])
            last = nums[-1]
            L2 = [[last] + e for e in L1]
            return L1 + L2
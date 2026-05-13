class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        postfix = 1
        # nums = [1,2,4,6]
        # prefix = 1 -> 1 -> 2 -> 8
        # postfix = 48 -> 24 -> 6 -> 1
        for i in range(len(nums)):
            res[i] *= prefix
            res[~i] *= postfix
            prefix *= nums[i]
            postfix *= nums[~i]
        return res
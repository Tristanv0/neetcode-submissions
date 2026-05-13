class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsVisited = {}

        for i in range(len(nums)):
            if target - nums[i] in numsVisited:
                return [numsVisited[target-nums[i]], i]
            else:
                numsVisited[nums[i]] = i

        
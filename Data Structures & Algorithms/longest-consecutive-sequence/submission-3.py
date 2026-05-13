class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(list(set(nums)))
        maxSeq = 0
        currSeq = 1
        prev = nums[0]
        print(f'{nums=}')
        for i in range(1, len(nums)):
            print(f'{nums[i]=}')
            print(f'{prev=}')
            if nums[i] == prev+1:
                currSeq += 1
                prev = nums[i]
            else: # nums[i] != prev-1
                if currSeq > maxSeq:
                    maxSeq = currSeq
                currSeq = 1
                prev = nums[i]
        print(f'{currSeq=}')
        return max(maxSeq, currSeq)
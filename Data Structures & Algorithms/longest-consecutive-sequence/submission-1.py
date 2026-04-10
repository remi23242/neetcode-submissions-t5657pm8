class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result=set(nums)
        streak=0
        for num in result:
            if (num-1) not in result:
                length=1
                while(num+length) in result:
                    length+=1
                streak=max(length,streak)
        return streak






        
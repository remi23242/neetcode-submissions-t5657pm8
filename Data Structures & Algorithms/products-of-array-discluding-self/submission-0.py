class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count=0
        result = []
        for n in range(len(nums)):
            if n==0:
                count=1
                
            else:
                count*=nums[n-1]
            result.append(count)
            
        
        for n in range(len(nums)-1,-1,-1):
            if n==len(nums)-1:
                count=1
                
            else:
                count*=nums[n+1]
            result[n]*=count
        return result
            


        
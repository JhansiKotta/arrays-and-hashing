class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod,count=1,0
        n=len(nums)
        res=[0]*n
        for num in nums:
            if num:
                prod*=num
            else:
                count+=1
        if count>1: return [0]*n
        for i ,c in enumerate(nums):
            if count: res[i]=0 if c else prod
            else: res[i]=prod//c 
        return res
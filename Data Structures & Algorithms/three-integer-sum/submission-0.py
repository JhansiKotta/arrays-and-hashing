class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            while l<r:
                curr=nums[i]+nums[l]+nums[r]
                if curr==0:
                    sub=sorted([nums[i],nums[l],nums[r]])
                    if sub not in ans:
                        ans.append(sub)
                    l+=1
                    r-=1
                elif curr<0:
                    l+=1
                else:
                    r-=1
        return ans        





                    

        
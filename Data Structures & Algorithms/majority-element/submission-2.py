class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=defaultdict(int)
        res=0 
        max=0
        for num in nums:
            d[num]+=1
            if max<d[num]:
                res=num
                max=d[num]
        return res

     

    

        
        
       
       
         
                
        
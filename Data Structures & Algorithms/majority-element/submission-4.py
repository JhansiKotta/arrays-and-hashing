class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        res=0 
        max=0
        for num in nums:
            d[num]=d.get(num,0)+1
            if max<d[num]:
                res=num
                max=d[num]
        return res

     

    

        
        
       
       
         
                
        
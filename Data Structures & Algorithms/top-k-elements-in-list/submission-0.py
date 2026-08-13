class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        
        for i in nums:
            d[i]+=1
        sorteditems=sorted(d,key=d.get,reverse=True)
        return sorteditems[:k]
        
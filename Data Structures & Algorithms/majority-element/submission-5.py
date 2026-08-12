class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        res = 0
        max_count = 0

        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

            if max_count < d[num]:
                res = num
                max_count = d[num]

        return res
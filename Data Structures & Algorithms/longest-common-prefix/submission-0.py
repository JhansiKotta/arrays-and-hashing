class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        small=strs[0]
        for w in strs:
            if len(w)<len(small):
                small=w
        ans=""
        for i in range(len(small)):
            for w in strs:
                if w[i]!=small[i]:
                    return ans
            ans+=small[i]
        return ans

        
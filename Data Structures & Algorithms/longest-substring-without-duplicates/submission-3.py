class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cset = set()
        l,r = 0,0
        
        
        ans = 0
        for r in range(len(s)):
            while s[r] in cset:
                cset.remove(s[l])
                l+=1
            
            cset.add(s[r])

            ans = max(ans,r-l+1)
        
        return ans
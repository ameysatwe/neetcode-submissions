class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        mp = {}

        for n in nums:
            if n in mp:
                return True
            else:
                mp[n] = 1
        
        return False
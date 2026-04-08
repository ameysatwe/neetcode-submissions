class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        l = 0

        for n in ns:
            if (n-1) not in ns:
                le=1
                while n+le in ns:
                    le+=1
                l = max(le,l)
        return l
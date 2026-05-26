class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for w in strs:
            s_word = str(sorted(w))
            ans[s_word].append(w)
        
        return list(ans.values())
        

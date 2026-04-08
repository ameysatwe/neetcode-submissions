class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_list = defaultdict(list)

        for word in strs:
            s_word = str(sorted(word))
            freq_list[s_word].append(word)
        
        return list(freq_list.values())
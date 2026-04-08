class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_list = defaultdict(list)

        for word in strs:
            s_word = str(sorted(word))
            # if s_word in freq_list:
            freq_list[s_word].append(word)
            # else:
                # freq_list[s_word] = [word]
        
        return list(freq_list.values())
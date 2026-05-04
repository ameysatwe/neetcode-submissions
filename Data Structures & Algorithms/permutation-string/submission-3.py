class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1cnt = Counter(s1)
        window = len(s1)

        for i in range(len(s2)-window+1):
            print(s2[i:i+window])
            s2cnt = Counter(s2[i:i+window])

            if s1cnt == s2cnt:
                return True
        
        return False

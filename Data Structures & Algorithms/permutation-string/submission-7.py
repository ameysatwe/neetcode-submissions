class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1cnt = Counter(s1)
        window = len(s1)

        s2cnt = Counter(s2[0:window])
        if s1cnt == s2cnt:
            return True

        for i in range(window,len(s2)):
            s2cnt[s2[i]] += 1
            s2cnt[s2[i-window]]-=1

            if s2cnt[s2[i-window]] == 0:
                del s2cnt[s2[i-window]]
            if s1cnt == s2cnt:
                return True

        
        return False

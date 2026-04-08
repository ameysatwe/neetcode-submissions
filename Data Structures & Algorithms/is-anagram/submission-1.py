class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        

        s_mp = {}
        t_mp = {}

        for w in s:
            if w in s_mp:
                s_mp[w] +=1
            else:
                s_mp[w] = 1

        for w in t:
            if w in t_mp:
                t_mp[w] +=1
            else:
                t_mp[w] = 1

        return s_mp == t_mp
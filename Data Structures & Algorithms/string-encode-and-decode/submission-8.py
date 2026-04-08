class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""

        for st in strs:
            ans += str(len(st)) + "#" + st
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        print(s)
        i = 0
        jmp = ""
        while i<len(s): 
            if s[i] == "#":
                jmp = int(jmp)
                ans.append(s[i+1:i+jmp+1])
                i += jmp
                jmp = ""
            elif s[i].isdigit():
                jmp += s[i]
            i+=1
        return ans



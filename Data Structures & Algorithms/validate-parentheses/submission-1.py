class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        ctop = {")":"(","}":"{","]":"["}

        for c in s:
            if c in ctop:
                if st and st[-1]==ctop[c]:
                    st.pop()
                else:
                    return False
            
            else:
                st.append(c)


        return True if not st else False
            
            

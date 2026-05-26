class Solution:
    def isValid(self, s: str) -> bool:
        
        st = []

        cto = {
            "]":"[",
            "}":"{",
            ")":"("
        }

        for c in s:
            if c in cto:
                if st and cto[c] == st[-1]:
                    # return False
                    st.pop()
                else:
                    return False
            else:
                st.append(c)

            # st.pop()
        
        return not st
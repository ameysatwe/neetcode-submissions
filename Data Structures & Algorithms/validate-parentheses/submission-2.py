class Solution:
    def isValid(self, s: str) -> bool:
        st = []


        close_to_open = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for c in s:
            if c in close_to_open:
                if st and st[-1] == close_to_open[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        

        return True if not st else False
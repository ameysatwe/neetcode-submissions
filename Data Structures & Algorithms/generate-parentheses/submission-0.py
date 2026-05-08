class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        st = []

        def bt(op,close):
            if op == close ==n:
                res.append("".join(st))
                return
            
            if op<n:
                st.append("(")
                bt(op+1,close)
                st.pop()
            if close<op:
                st.append(")")
                bt(op,close+1)
                st.pop()
        

        bt(0,0)

        return res
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []


        for i,t in enumerate(temperatures):
            while st and st[-1][0]<t:
                stackT,stackI = st.pop()
                res[stackI] = i - stackI
            st.append((t,i))

        
        return res
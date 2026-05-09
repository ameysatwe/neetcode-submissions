class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dtoC = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"qprs",
            "8":"tuv",
            "9":"wxyz",
        }

        def bt(i,curr_str):
            if len(curr_str) == len(digits):
                res.append(curr_str[:])
                return
            
            for c in dtoC[digits[i]]:
                bt(i+1,curr_str+c)
        
        if digits:
            bt(0,"")
        
        return res
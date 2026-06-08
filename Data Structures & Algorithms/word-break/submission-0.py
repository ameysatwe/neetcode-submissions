class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)

        dp[n] = True

        for i in range(n-1,-1,-1):
            for w in wordDict:
                lw = len(w)
                if i+lw<=n and s[i:i+lw] == w:
                    dp[i] = dp[i+lw]

                if dp[i]:
                    break
        
        return dp[0]
                 
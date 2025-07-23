class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # Create a 2D DP table (m+1) x (n+1), initialized to False
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string and empty pattern match
        dp[0][0] = True

        # If pattern starts with *, it can match the empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Fill the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # * matches zero characters (dp[i][j - 1]) OR one or more characters (dp[i - 1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    # Direct match or single-character wildcard '?'
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]
        

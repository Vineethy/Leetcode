class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

    # dp[i][j] = does s[0..i-1] match p[0..j-1]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True  # empty string and pattern match

    # Handle patterns like a*, a*b*, etc. matching empty string
        for j in range(2, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

    # Fill the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                # Zero occurrences
                    dp[i][j] = dp[i][j - 2]
                # One or more occurrences
                    if p[j - 2] == s[i - 1] or p[j - 2] == ".":
                        dp[i][j] |= dp[i - 1][j]

        return dp[m][n]

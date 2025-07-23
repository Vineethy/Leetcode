class Solution(object):
    def longestPalindrome(self, s):
        if not s or len(s) == 1:
            return s

        start, end = 0, 0

        def expandFromCenter(left, right):
            # Expand as long as it's a palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1  # return the valid palindrome bounds

        for i in range(len(s)):
            # Odd length palindromes
            l1, r1 = expandFromCenter(i, i)
            # Even length palindromes
            l2, r2 = expandFromCenter(i, i + 1)

            # Choose the longer palindrome
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]
        
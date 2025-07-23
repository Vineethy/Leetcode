class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: str, open_count: int, close_count: int):
            # Base case: if the string is complete
            if len(current) == 2 * n:
                result.append(current)
                return

        # If we can still add '(', do it
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)

        # If we can add ')', only if it won’t unbalance
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)

        backtrack("", 0, 0)
        return result    

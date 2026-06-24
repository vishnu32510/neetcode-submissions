class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed_par = {'}' : '{', ')':'(', ']':'['}

        for c in s:
            if c in closed_par:
                if stack and stack[-1] == closed_par[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
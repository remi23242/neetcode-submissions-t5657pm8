class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openandclose={')':'(',']':'[','}':'{'}
        for c in s:
            if c in openandclose:
                if stack and stack[-1]==openandclose[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack

        
        
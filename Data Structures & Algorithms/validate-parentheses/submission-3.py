class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b == "{" or b == "(" or b == "[":
                stack.append(b)
            elif len(stack) != 0:
                if b == "}":
                    if stack.pop() != "{":
                        return False
                elif b == ']':
                    if stack.pop() != '[':
                        return False
                elif b == ')':
                    if stack.pop() != '(':
                        return False
            else:
                return False
            
        return len(stack) == 0


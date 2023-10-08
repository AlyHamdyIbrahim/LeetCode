class Solution:
    def isValid(self, s: str) -> bool:
        sLength = len(s)
        if sLength % 2 != 0:
            return False
        
        stack = []

        for i in range(sLength):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if s[i] == ')' and stack[-1] != '(':
                    return False
                if s[i] == '}' and stack[-1] != '{':
                    return False
                if s[i] == ']' and stack[-1] != '[':
                    return False
                stack.pop()

        return True if len(stack) == 0 else False

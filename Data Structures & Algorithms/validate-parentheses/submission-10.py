class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for char in s:
            if char in ['(', '[','{']:
                stack.append(char)
            elif char not in ['(', '[','{']:  
                if len(stack) == 0:
                    return False
                top_stack = stack[-1]
                if top_stack == '(' and char != ')':
                    return False
                elif top_stack == '[' and char != ']':
                    return False
                elif top_stack == '{' and char != '}':
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False
class Solution:
    def isValid(self, s: str) -> bool:
        new_stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}
        for char in s:
            if char in closeToOpen:
                if new_stack and new_stack[-1] == closeToOpen[char]:
                    new_stack.pop()
                else:
                    return False
            else:
                new_stack.append(char)
        return True if not new_stack else False




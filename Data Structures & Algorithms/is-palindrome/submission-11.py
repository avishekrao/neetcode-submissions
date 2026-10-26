class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''.join(char for char in s if char.isalnum()).lower()
        new_str_len = len(new_str)
        for index in range((new_str_len + 1) // 2):
            if new_str[index] != new_str[new_str_len - index - 1]:
                return False
        return True
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        is_palindrome = True
        for i in range(len(x) // 2):
            if x[i] != x[-1 - i]:
                is_palindrome = False
                break
        return is_palindrome

#s = Solution()
#print(s.isPalindrome(-1221))
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 and x > (2**31):
            return False
        elif str(x) == str(x)[::-1]:
            return True
        return False

output = Solution();

print(output.isPalindrome(121)) 
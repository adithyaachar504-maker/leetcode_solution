class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        x=str(x)
        while x>0:
            
            if x==x[::-1]:
                return True
            else:
                 return False
x=121
solution=Solution()
result=solution.isPalindrome(x)
print(result)


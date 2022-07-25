class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        numarray = list(map(int, str(x)))
        l_numarray = len(numarray)
        for i in range(l_numarray//2):
            if numarray[l_numarray-i-1] != numarray[i]:
                return False
        return True

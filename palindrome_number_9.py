class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        numarray = list(map(int, str(x)))
        print(numarray)
        l_numarray = len(numarray)
        for i in range(l_numarray):
            if numarray[l_numarray-i-1] != numarray[i]:
                return False
        return True

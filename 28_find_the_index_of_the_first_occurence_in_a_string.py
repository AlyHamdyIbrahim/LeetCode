class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystackLength = len(haystack)
        needleLength = len(needle)

        if needleLength > haystackLength:
            return -1
        
        for i in range(haystackLength - needleLength + 1):
            if haystack[i:i+needleLength] == needle:
                return i
        
        return -1

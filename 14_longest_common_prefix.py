class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        match = True
        shortestLength = 100
        listLength = len(strs)
        for i in range(listLength):
            if len(strs[i]) < shortestLength:
                shortestLength = len(strs[i])
        i = 0
        while match and (i < shortestLength):
            for j in range(listLength - 1):
                if strs[j][i] != strs[j + 1][i]:
                    match = False
                    break
            if match:
                i += 1
        print(i)
        return strs[0][:i]
    
# print(Solution().longestCommonPrefix(["flower","flow","flight"]))

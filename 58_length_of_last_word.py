class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        count = 0
        for i in range(-1, -len(s) - 1 ,-1):
            if s[i] == " " and count != 0:
                return count
            elif s[i] != " ":
                count += 1
        return count

        # ---------------Other Solution---------------
        # s = s[::-1]
        # count = 0
        # for i in range(len(s)):
        #     if s[i] == " " and count != 0:
        #         return count
        #     elif s[i] != " ":
        #         count += 1
        # return count
        #---------------------------------------------
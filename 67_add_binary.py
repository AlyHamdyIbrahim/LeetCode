class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        c = ""
        aLength = len(a)
        bLength = len(b)
        for i in range(-1, -1 * max(aLength, bLength) -1, -1):
            aDigit = int(a[i]) if i >= (-1*aLength) else 0
            bDigit = int(b[i]) if i >= (-1*bLength) else 0
            sum = aDigit + bDigit + carry
            c = str(sum % 2) + c
            carry = sum // 2
        return str(carry) + c if carry == 1 else c
    
    # ---------------Other Solution---------------
    #   return bin(int(a,2)+int(b,2))[2:]
    #---------------------------------------------
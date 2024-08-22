class Solution:
    def findComplement(self, num: int) -> int:
        
        s = bin(num)[2:]
        arr = ""
        for i in range(len(s)):
            q = s[i]
            if q == "1":
                arr += "0"
            else:
                arr += "1"
        val = 0
        cnt = len(arr)-1
        for i in range(0, len(arr)):
            val = val + ((2**cnt) * int(arr[i]))
            cnt -= 1
        return val
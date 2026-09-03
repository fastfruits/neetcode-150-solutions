class Solution:
    def reverseBits(self, n: int) -> int:
        newN = 0

        for i in range(32):
            bit = n & 1 #Extract the lowest bit of n
            newN = (newN << 1) | bit #Insert the bit
            n >>= 1 #Discard the last bit

        return newN
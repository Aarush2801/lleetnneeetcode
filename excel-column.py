'You are given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.'

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            res+= chr(ord('A') + offset)
            columnNumber = (columnNumber-1)//26

        return res[::-1]


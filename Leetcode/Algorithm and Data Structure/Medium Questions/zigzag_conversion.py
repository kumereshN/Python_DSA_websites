def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows < 2:
        return s
    i = 0
    res = [""]*numRows      # We will fill in each line in the zigzag
    for letter in s:
        if i == numRows-1:  # If this is the last line in the zigzag we go up, because 0 --> Line 1, 1 ---> Line 2, 2 ---> Line 3 when numRows = 3
            grow = False
        elif i == 0:        #Otherwise we continue to go down
            grow = True
        res[i] += letter    #Add the letter to its row
        i = (i+1) if grow else i-1  # We increment (add 1) if grow is True,
    	                            # and decrement otherwise

    return "".join(res)     # return the joined rows

s = "PAYPALISHIRING"
numRows = 3
convert(s, numRows)

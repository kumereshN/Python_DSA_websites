def str2int(num):
    result = 0
    for n in num:
        result = result * 10 + ord(n) - ord('0')
    return result

return str(str2int(num1) + str2int(num2))

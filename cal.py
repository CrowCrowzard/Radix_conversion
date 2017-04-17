def conv10(n):
    _len = len(n)
    conv_10 = 0
    for i in range(_len):
        conv_10 += (ord(n[_len-i-1])-ord('A')) * (26 ** i)
    return conv_10

def conv26(n):
    conv_26 = ""
    while n >= 26:
        conv_26 += chr(int((n % 26) + ord('A')))
        n /= 26
    conv_26 += chr(int(n + ord('A')))
    return "".join(reversed(conv_26))


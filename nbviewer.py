__doc__ = """Python 2/3 compatible"""
def int2base26(x, base=26):
    import string
    digs = [string.ascii_letters][0][:26]
    if x < 0:
        sign = -1
    elif x == 0:
        return 0
    else:
        sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)

if __name__ == "__main__":
    dimensions = 60
    length_of_board = 240/dimensions
    width_of_board = 180/dimensions
    words = []
    try:
        for i in xrange(1, (26**int(length_of_board))+1):
            words.append(int2base26(i))
    except:
        for i in range(1, (26**int(length_of_board))+1):
            words.append(int2base26(i))

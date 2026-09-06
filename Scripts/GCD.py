def GCD(x, y):
    def _GCD(b, s): # actual GCD
        if (s == 0): return b
        b = b % s
        if (b < s):
            return _GCD(s, b)
        return _GCD(b, s)

    if (x >= y): # sorter
        return _GCD(x, y)
    return _GCD(y, x)

from GCD import GCD

def xGCD(a, b): # ax + bx = gcd(a, b)
    x = [1, 0]
    y = [0, 1]
    r = []
    if a > b:
        r = [a, b]
    else:
        r = [b, a]
    gcd = GCD(a, b)
    def _xGCD(r, x, y): # actual xGCD
        if r[1] == gcd or r[0] == 0: return (gcd, (x[1], y[1]))
        # (gcd, (Coef for bigger integer, Coef for smaller integer))
        q = r[0] // r[1]

        xCoef = x[0] - q * x[1]
        x[0] = x[1]
        x[1] = xCoef
        yCoef = y[0] - q * y[1]
        y[0] = y[1]
        y[1] = yCoef

        r2 = r[0] - q * r[1]
        r[0] = r[1]
        r[1] = r2

        return _xGCD(r, x, y)
    return _xGCD(r, x, y)

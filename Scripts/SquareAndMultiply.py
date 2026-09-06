def SquareAndMultiply(N, x): # N^x
    digits = list(bin(x)[2:]) # 1. Converts expoenent to binary
    sum = N
    for i in range(1, len(digits)): # 2. Iterate the binary and perform actions based on number
        sum = sum ** 2
        if digits[i] == "1":
            sum = sum * N
    return sum

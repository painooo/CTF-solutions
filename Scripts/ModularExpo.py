def ModularExpo(N, x, m): # N^x % m
    if m == 1:
        return 0
    digits = list(bin(x)[2:]) # 1. Convert to binary
    sum = N
    for i in range(1, len(digits)): # Apply (A * B) mod C = ((A mod C) * (B mod C)) mod C
        sum = (sum % m) ** 2 
        if digits[i] == "1":
            sum = (sum % m) * (N % m)
    return sum % m

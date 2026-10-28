# Square and Multiply

- This algorithm reduces the steps needed to exponentiate a number
    - In cryptography, lots of numbers will have giant exponents and it's best to be able to calculate them quickly
1. Convert exponent to a binary number
2. Iterate the binary
    1. First 1 means to simply set the number (N)
    2. Following 0 means to square the number (N)^2
    3. Following 1 means to square and multiply the number (N)^2*N

[Script](../Scripts/SquareAndMultiply.py)


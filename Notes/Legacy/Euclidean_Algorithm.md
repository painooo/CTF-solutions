# Euclidean Algorithm
> An efficient way to calcuate the GCD of two numbers

- Idea is the GCD won't change if the bigger of the two numbers is replaced with their difference
    - Use the modulus operator since the difference is basically the remainder of the two numbers (bigger / smaller)
- This idea can then be repeated until the smaller number equates 0 where the bigger number is then the GCD

[Script](../Scripts/GCD.py)

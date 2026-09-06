# Converting Between Bases

> Any base can be converted into an integer
>
> Any integer can be converted into a base

- The idea comes from how base2 is converted into base10 and vice versa
    - Base2 -> Base10
        - For each character from the rightest-most point
        - Get the index of the character in the Base2 set
        - Multiply that index by the length of the Base2 set to the power of the place of the character (starting from 0)
            - index * len(Base2 set) ** characterIndex
    - Base10 -> Base2
        - Get the remainder (r) and quotient (q) of the integer divided by the length of the Base2 set
        - r is then the index of the charater
        - q is the new integer
        - Repeat the process until q is equal to 0
        - r is given in reverse so we'll need to reverse the resulting list

[Script](../Scripts/conver.py)

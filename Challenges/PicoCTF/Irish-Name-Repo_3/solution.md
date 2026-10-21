# Irish-Name-Repo 3
- Goal: Login as admin
1. Website seemed the same as the previous Irish-Name-Repo so jumped straight to login page
    - Greeted by a form which only takes password
2. Checked network tab under devtools to see if it truly takes only password
    - Bad News: It does only
3. Tested different SQLi payloads to identify vulnerabilities
    - `'` single quote
        - Returned 500 server error 
        - It's still vulnerable to SQLi
    - `' OR '1'='1' -- -` & `' OR '1'='1`
        - Returned 500 server error
        - Why?
    - `' -- -`
        - Returned login failed
        - Means it successfully went through
        - Why does it take this, but not with the keyword?
4. Haven't bother before, but the earlier network tab also revealed a debug parameter
    - Setting debug=1 reveals password is encrypted in someway before being processed
    - OR -> BE
    - abc -> nop
    - abcdefghijklmnopqrstuvwxyz -> nopqrstuvwxyzabcdefghijklm
        - Seems to be a type of substitution cipher
    - Using the substitution alphabet, crafted the payload `' BE 1=1-- -`
## Solution
- Insert `' BE 1=1-- -` into the only parameter

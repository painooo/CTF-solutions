# Irish-Name-Repo 2
- Goal: Login as admin
1. The website resembled Irish-Name-Repo 1 and so I jumped straight to SQLi on the login page with the same payload `' OR '1'='1'-- -`
    - Website returned `SQLi detected`
2. In order to bypass this I tried looking for what triggered the message
    - `'` single quote inserted into either parameters
        - Returned 500 server error
        - SQLi is still possible
        - Doesn't trigger the message
    - `'` single quote inserted into both parameters
        - Returned`Login failed.`
        - SQL query is most likely something like `SELECT * FROM users WHERE username='$user' AND password='$pass'`
            - `SELECT * FROM users WHERE username='`**'**`' AND password='`**'**`'` which closes incomplete quotes
            - **Based on this query, if we were to inject a proper username and comment the rest out the query should be valid**
              - `admin' -- -`
              - `admin` because under the support page an admin user is defined
    - `' <keyword>` inserted into either parameters
        - **Any SQL keyword yielded `SQLi detected`**
        - Any non SQL keyword yielded 500 server error
## Solution
- Inject `admin'-- -` into username parameter in the login page

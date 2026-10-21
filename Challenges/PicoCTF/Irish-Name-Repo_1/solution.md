# Irish-Name-Repo 1
- Goal: Login as admin
1. I started by looking around the website
    - Checked the images to see if they were vulnerable to LFI (e.g `image?file=`)
    - Under support.html, a user had issue with Conan O'Brian regarding a SQL error

## Solution
- Knowing a SQL error may indicate SQLi I injected `' OR '1'='1'-- -` into the admin login page which worked!  

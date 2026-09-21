# XXE Infiltration Lab

1. During the attacker's port scan, what is the highest-numbered TCP port that responded as open on the victim host?
    - In TCP, to establish a connection one would use a 3-way handshake
        - SENDER:**SYN**, RECIEVER:**SYN-ACK**, SENDER:**ACK**
    - To find which ports are open we just have to find when the RECIEVER sends **SYN-ACK**
    - In Wireshark, we can use `tcp.flags.syn == 1 && tcp.flags.ack == 1`
    - I simply scrolled through the SYN, RST-ACK till I found a SYN-ACK
    - Answer: `3306`

2. By identifying the vulnerable PHP script, security teams can directly address and mitigate the vulnerability. What's the complete URI of the PHP script vulnerable to XXE Injection?
    - XXE injection is related to XML, typically in HTTP requests
    - Scrolling through HTTP requests we'd find `/review/upload.php` where the attacker performed XXE injection
    - Answer: `/review/upload.php`

3. To construct the attack timeline and determine the initial point of compromise. What's the name of the first malicious XML file uploaded by the attacker?
    - Look for the first request to `/review/upload.php`
    - Answer: `TheGreatGatsby.xml`

4. Understanding which sensitive files were accessed helps evaluate the breach's potential impact. What's the name of the web app configuration file the attacker read?
    - Sift through requests to `/review/upload.php` for requests which use XXE injection to open config files
    - Answer: `config.php`

5. To assess the scope of the breach, what is the password for the compromised database user?
    - In the 200 OK response after the request in Question #4
    - Answer `Winter2024`

6. After stealing the credentials from the config file, the attacker authenticates to the MySQL service on the victim. 
    - A little after the request in Question #5, under protocol, should be MySQL
    - Login requests have under the `Info` tab: Login Request
    - Time stamp can be found under `Time`
    - Answer: `2024-05-31 12:08`

7. To eliminate the threat and prevent further unauthorized access, can you identify the name of the web shell that the attacker uploaded for remote code execution and persistence?
    - A web shell allows an attack to execute commands on the server
    - Answer `booking.php`

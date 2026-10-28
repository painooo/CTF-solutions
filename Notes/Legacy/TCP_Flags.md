# TCP Flags
- The TCP Header contains 8 1-bit (control bit) reserved for setting flags
    - [CWR, ECE, URG, ACK, PSH, RST, SYN, FIN]
    - Ex) 00010010 -> SYN-ACK
- Control bits are managed by [IANA](https://www.iana.org/assignments/tcp-parameters#tcp-header-flags) [SRC](https://www.rfc-editor.org/rfc/rfc9293.html) 
1. CWR: Congestion Window Reduced
2. ECE: ECN-Echo
3. URG: Urgent
    - Marks the urgent field as important
4. ACK: Acknowledgement
    - Marks the acknowledgement field as important
        - Used to acknowledge the sequence numbers received  
5. PSH: Push
    - Asks for the other end to send the buffered data
6. RST: Reset
    - Resets the connection
7. SYN: Synchronize
    - Synchronizes the sequence number
        - Used to order packets
8. FIN: Finish
    - Sender has no more data to send

- In a 3-way handshake why do both sender and reciever need to send each other their initial sequence number (ISN)?
    - It's so down the line, they can acknowledge each others previous packet

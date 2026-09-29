Plan: Have a way to organize data for CTFs
- What kind of data?
    - Solutions
    - Challenges
    - Notes
    - Scripts
1. Seperate challenges by CTF
    - If a solution references a note it should link to it
    - Challenges/
        - CTFA/
            - ChallengeA/
                - script.py
                - solution.md
            - ChallengeB/
        - CTFB/
            - ChallengeA/
2. Centralize all notes and scripts
    - If a note has a script it should link to it
    - Notes are created by..
        1. Noting everything down
        2. Revising wording and facts
        3. Seperating them by headers based on their content (same content together) 
    - Notes/
        - Format: `Concept \n Information`
        - conceptA.md
        - conceptB.md
        - conceptC.md
    - Scripts/
        - Scripts should be documented
        - FunctionA.py
        - FunctionB.py
        - FunctionC.py

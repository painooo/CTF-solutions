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
    - Notes should follow the concept of first-come-is-created & last-file-is-linked
    - After creating notes it should be decoupled for easy reference & link
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

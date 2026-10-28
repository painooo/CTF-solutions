# Plan: Have a way to organize CTF files, scripts, and data
- Challenges/ -> Stores a catalog of CTFs
    - 'CTF'/ -> Stores a list of challenges
        - 'challenge'/
            - Each challenge must contain a `solution.md` file and may include scripts or other files
            - `solution.md` -> should show goal, process, and solution
              - Be specific about the goal to best fit the challenge (goal may change)
            ```
            # challenge_name
            - Goal: solve this challenge
            1. Found this which tells us to do this
            2. Found that
            3. Tried this 
            4. Tried this which basically does this
            
            ## Solution
            1. Do this
            2. Inject this
            3 Voila. Solved
            ```
- Scripts/ -> Stores random scripts I wrote and don't wanna write again
- Notes/ -> Stores notes
    - Each note is then seperated by its source
    - resource/ -> Stores notes related to that resource
        - `src.txt` -> Stores the link to the resource
        - Notes are named according to the resource module or their purpose (e.g. A note all about the inner workings of car engines will be named "car-engine.md")
        - Notes are created by..
            1. "Globbing" together information in bullet points, no thinking should be required, just bullet
            ```
            # Note (temp)
            - Info_A
            - Equation_B
            - Script_A
            - Info_C
            - Info_B
            - Script_B
            - Script_C
            ```
            2. Determine purpose & if it has to seperated
            ```
            Purpose: A, B, & C
            ```
            3. Revise & seperate information based on that purpose
            ```
            # Note A
            - Info_A
            - Script_A
            ```
            ```
            # Note B
            - Info_B
            - Script_B
            - Equation_B
            ```
            ```
            # Note C
            - Info_C
            - Script_C
            ```

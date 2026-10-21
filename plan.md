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
- Scripts/ -> Stores random collection of notes from `Notes/`
- Notes/ -> Stores notes
  - Groups of notes are seperated by source
  - 'source'/
    - Each note is seperated & titled by topic and/or purpose usually defined by the source
    - Example `note.md`
    ```
    # note_title
    - Dilly Dally
    - `Ax + Bx = Cx`
    - In 1939, asdas
    ```


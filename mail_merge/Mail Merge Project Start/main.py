PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_files:
    names = names_files.readlines()

with open("./Input/Letters/starting_letter.txt") as letters_files:
    letter = letters_files.read()
    for name in names:
        n = name.strip()
        new_letter = letter.replace(PLACEHOLDER, n)
        with open(f"./Output/ReadyToSend/letter_for_{n}.txt", "w") as completed_file:
            completed_file.write(new_letter)

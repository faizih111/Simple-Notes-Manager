print("--- Notes Manager ---")
print("1. Write a new note")
print("2. Read all notes")
print("3. Add another note")
print("4. Delete notes file")
print("5. Exit\n")

option = int(input("Enter your option: "))

if option == 1:
    with open("notes.txt", "w") as f:
        f.write(input("Enter your notes: "))
        print("Note saved successfully!")

if option == 2:
    with open("notes.txt") as f:
        print(f"Your notes: {f.read()}")

if option == 3:
    with open("notes.txt", "a") as f:
        f.write(input("Enter your new note: "))
        print("Note added successfully!")

if option == 4:
    import os
    os.remove("notes.txt")
    print("Notes file deleted successfully!")

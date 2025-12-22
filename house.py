from unittest import case

()
name = input("What's your name? ").lower().strip()

match name:
    case "harry" | "hermione" | "ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
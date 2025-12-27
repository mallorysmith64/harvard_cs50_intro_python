name = input("What's your name? ")

with open("names.csv", "a") as file:
    file.write(f"{name}\n"     )
    
names = []
with open("names.csv", "r") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names):
    print(f"hello, {name}")
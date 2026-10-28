# Program to remove blank lines from a text file

with open("input.txt", "r") as file:
    lines = file.readlines()

with open("output.txt", "w") as file:
    for line in lines:
        if line.strip():
            file.write(line)

print("Blank lines removed successfully!")
print("Cleaned content saved in output.txt")

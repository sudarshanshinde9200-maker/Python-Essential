filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        contents = file.read()

    print("File Contents:")
    print(contents)

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission denied")
from .readers import txt_reader

print("Hello, welcome to the word-list curator CLI")
print("Please enter the file path you'd like to extract text from")
file = input("Path: ")
print()
print("What file reader would you like to use?")
print("1 - .txt")

choice = 0
while choice < 1 or choice > 1:
    choice = int(input(": "))


match choice:
    case 1:
        txt_reader.main(file)
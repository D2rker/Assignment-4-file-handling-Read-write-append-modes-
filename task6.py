import os

filename = input("Enter the filename you wish to open: ")

if os.path.exists(filename):
    print(f"\n--- Opening {filename} ---")
    with open(filename, "r") as file:
        content = file.read()
        print(content)

else:
    print("File not found. Please check the filename.")
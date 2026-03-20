# Task 2: Read fiel in diffent ways.


filename = "sales_data.txt"

print("--- Method 1: .read() ---")
with open(filename, "r") as file:
    entire_content = file.read()
    print(entire_content)

print("--- Method 2: .readline() ---")
with open(filename, "r") as file:
    first_line = file.readline().strip()  # .strip() removes the newline character
    print(f"First line: {first_line}")

print("\n--- Method 3: .readlines() to Integers ---")
with open(filename, "r") as file:
    lines = file.readlines()

    sales_integers = []
    for line in lines:
        clean_line = line.strip()
        if clean_line:  # Check if the line is not empty
            sales_integers.append(int(clean_line))

    print(f"List of integers: {sales_integers}")

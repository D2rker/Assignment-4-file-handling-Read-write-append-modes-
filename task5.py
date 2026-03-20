filename = "products.txt"


with open(filename, "w") as file:
    print("Please enter information for 3 products:")
    for i in range(1, 4):
        name = input(f"Enter name for product {i}: ")
        price = input(f"Enter price for product {i}: ")

        file.write(f"{name} | {price}\n")

print("\nFile 'products.txt' has been created.\n")

print("--- Current Product List ---")
with open(filename, "r") as file:
    for line in file:
        # .strip() removes the newline character for a clean print
        print(line.strip())
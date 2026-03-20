filename = "sales_data.txt"
new_sales = [5000, 2500, 1700]

with open(filename, "a") as file:
    for sale in new_sales:
        file.write(str(sale) + "\n")

print("--- Updated sales_data.txt ---")
with open(filename, "r") as file:
    content = file.read()
    print(content)

with open(filename, "r") as file:
    line_count = len(file.readlines())
    print(f"Total number of lines: {line_count}")
sales = [1200, 450, 980, 1500, 3000]

with open("sales_data.txt", "w") as file:
    for sale in sales:
        file.write(str(sale) + "\n")

print("Contents of sales_data.txt:")
with open("sales_data.txt", "r") as file:
    content = file.read()
    print(content)


with open("sales_data_comma.txt", "w") as file:
    comma_separated_sales = ", ".join(map(str, sales))
    file.write(comma_separated_sales)

print("Comma-separated version:")
with open("sales_data_comma.txt", "r") as file:
    print(file.read())
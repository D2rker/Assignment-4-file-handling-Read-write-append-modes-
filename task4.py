# Task 4: Generates report summary from a file.


filename = "sales_data.txt"
sales_list = []

with open(filename, "r") as file:
    for line in file:
        clean_line = line.strip()
        if clean_line:  # Ensures we don't try to convert empty lines
            sales_list.append(int(clean_line))

if sales_list:
    total_sales = sum(sales_list)
    highest_sale = max(sales_list)
    lowest_sale = min(sales_list)
    average_sale = total_sales / len(sales_list)

    print("--- Sales Summary Report ---")
    print(f"Total Sales:   {total_sales}")
    print(f"Highest Sale:  {highest_sale}")
    print(f"Lowest Sale:   {lowest_sale}")
    print(f"Average Sale:  {average_sale:.2f}") # Rounds to 2 decimal places
else:
    print("The file is empty. No data to process.")

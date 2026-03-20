prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount_percent = float(input("Enter the discount percentage (e.g., 10 for 10%): "))

filename = "discount_report.txt"
discounted_prices_list = []

with open(filename, "w") as file:
    # Header for clarity
    file.write("Product | Original Price | Discounted Price\n")
    file.write("-" * 45 + "\n")

    for product, original_price in prices.items():
        discounted_price = original_price * (1 - (discount_percent / 100))
        discounted_prices_list.append(discounted_price)

        file.write(f"{product} | {original_price} | {discounted_price:.2f}\n")

    total_items = len(prices)
    average_discounted = sum(discounted_prices_list) / total_items

    file.write("-" * 45 + "\n")
    file.write(f"Total Items: {total_items}\n")
    file.write(f"Average Discounted Price: {average_discounted:.2f}\n")

print(f"\n--- {filename} Contents ---")
with open(filename, "r") as file:
    print(file.read())
# Define the prices dictionary
prices = {
    "Bubblegum": 2,
    "Toffee": 0.2,
    "Ice cream": 5,
    "Milk chocolate": 4,
    "Doughnut": 2.5,
    "Pancake": 3.2
}

# Print "Prices:" and then each item with its price
print("Prices:")
for item, price in prices.items():
    print(f"{item}: ${price}")

# Create month income dictionary
earnings = {
    "Bubblegum": 202,
    "Toffee": 118,
    "Ice cream": 2250,
    "Milk chocolate": 1680,
    "Doughnut": 1075,
    "Pancake": 80
}
# Print earned amount and earned table in the specified format

print("Earned amount:")
# Initialize a variable to keep track of the total income

total_income = 0.0
# Print each item with its earnings and calculate the total income
for item, amount in earnings.items():
    print(f"{item}: ${amount}")
    total_income += amount

# Print the total income
print(f"\nIncome: ${total_income}")

staff_expenses = int(input("Staff expenses:\n> "))
other_expenses = int(input("Other expenses:\n> "))

sum_expenses = staff_expenses + other_expenses

net_income = total_income - sum_expenses

# Print net income
print(f"Net income: ${net_income}")

#future code:

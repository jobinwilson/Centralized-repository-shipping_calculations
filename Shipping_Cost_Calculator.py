# Shipping Cost Calculator

# Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

# Calculate shipping cost
shipping_cost = weight * rate

# tax rate for shipping
tax_rate = 0.05

# add tax calculation
shipping_cost = shipping_cost + tax_rate*shipping_cost

# add a constatnt offset of $1
shipping_cost += 1

# Display the result
print(f"Total Shipping Cost: {shipping_cost} USD")

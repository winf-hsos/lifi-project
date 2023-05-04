# TODO: Get user input
distance = input("How many kilometers do you plan to drive (whole numbers only)? ")
consumption = input("How many liters per 100 km does your car consume? ")
price_per_liter = input("What is the price per liter gas? ")

# TODO: Convert input to numeric values
distance = int(distance)

# Replace any "," with "."
consumption = consumption.replace(",", ".")
consumption = float(consumption)

# Replace any "," with "."
price_per_liter = price_per_liter.replace(",", ".")
price_per_liter = float(price_per_liter)

# TODO: Caculate total costs
total_costs = round((distance / 100) * consumption * price_per_liter, 2)
 
# TODO: Print result
print(f"Great! Your total costs will be { total_costs } EUR.")
age = input("Please enter your age: ")
age = int(age)

# TODO: Determine ticket costs based on age
if age <= 12:
    ticket_costs = 5
elif age > 12 and age <= 64:
    ticket_costs = 10
else:
    ticket_costs = 7

# TODO: Print ticket costs
print(f"Your ticket will be { ticket_costs } EUR.")
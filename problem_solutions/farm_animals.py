# TODO: Get the number of cows, pig and chickens from the farmer
cows = input("How many cows? ")
pigs = input("How many pigs? ")
chickens = input("How many chickens? ")

cows = int(cows)
pigs = int(pigs)
chickens = int(chickens)

# TODO: Calculate the number of legs
def get_leg_count(cows, pigs, chickens):
    leg_count = (cows * 4) + (pigs * 4) + (chickens * 2)
    return leg_count

legs = get_leg_count(cows, pigs, chickens)

# TODO Print the number of legs to the console
print(f"Leg count: {legs}")

# Calculate a new leg count based on different values
new_legs = get_leg_count(100, 200, 1000)
print(f"New leg count: { new_legs }")
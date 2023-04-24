colors = { "orange", "orange", "orange", "green", "green", "green", "blue", "blue" }
print(colors) # Output: {'blue', 'orange', 'green'}

colors_list = [ "orange", "orange", "orange", "green", "green", "green", "blue", "blue" ]
colors_set = set(colors_list)
print(colors_set) # Output: {'blue', 'orange', 'green'}

# Dictionaries
codes = {"A" : "01000001", "B" : "01000010", "C" : "01000011"}

print(f"Dictionary: { codes }")

# Add a new entry to a dictionary
codes["D"] = "01000100"
print(f"Dictionary: { codes }")

#  Removing entries
removed = codes.pop("D")
print(f"Removed: { removed }")
print(f"Dictionary after removal of { removed }: { codes }")

# Updating entries
codes["C"] = "hello"
print(f"Updated dictionary:  { codes }")

# Check for existance
if 'D' in codes:
    print('D is in the dictionary')
else:
    print('D does not exist in the dictionary')
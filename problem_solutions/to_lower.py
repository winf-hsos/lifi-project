def to_lower(string):
    result = ""
    for char in string:
        if ord(char) >= 65 and ord(char) <= 90:
            # Convert uppercase letter to lowercase
            lowercase_char = chr(ord(char) + 32)
            result += lowercase_char
        else:
            # Add non-uppercase letter character to result
            result += char
    return result

test = "Hello World!"
test_lower = to_lower(test)
print(test_lower)
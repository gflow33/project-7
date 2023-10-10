text = """2023-10-10 14:18:37,20
2023-10-10 14:18:39,19
2023-10-10 14:18:42,19
2023-10-10 14:18:47,18
2023-10-10 14:18:49,18
2023-10-10 14:18:54,18
2023-10-10 14:18:57,18
2023-10-10 14:18:59,18
2023-10-10 17:13:10,18
2023-10-10 17:14:18,20
2023-10-10 17:16:04,18
2023-10-10 17:18:37,18
2023-10-10 17:19:35,19"""

# Split the text into lines
lines = text.split("\n")
# print(lines)
# Initialize lists to store items before and after the comma
items_before_comma = []
items_after_comma = []

# Split each line by comma and store the items
for line in lines:
    parts = line.split(',')
    # print(parts)
    # if len(parts) == 2:
    items_before_comma.append(parts[0].strip())
    items_after_comma.append(parts[1].strip())

# Print the two lists
print("Items before comma:")
print(items_before_comma)

print("\nItems after comma:")
print(items_after_comma)

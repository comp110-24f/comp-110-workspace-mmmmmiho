"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

ice_cream["mint"] = 3

ice_cream["pecan"]

# Access values by their key using subscript
print(ice_cream["chocolate"])

# Re-assign valuses by their key using assign
ice_cream["vanilla"] += 10

# Remove items by key using the pop method

# Test if a key is in the dictionary

# Loop through items using for-in loops
for flavor in ice_cream:
    print(flavor)
    # This prints only keys

total_numbers: int = 0
for flavor in ice_cream:
    total_numbers += ice_cream[flavor]
    print(total_numbers)


# The variables (e.g. flavor) iterates over

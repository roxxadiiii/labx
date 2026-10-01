notes = """

"""

# Define fuzzy set A.
# Each key represents an element, and its value represents
# the corresponding membership degree.
A = {
    1: 0.2,
    2: 0.5,
    3: 0.8,
}

# Define fuzzy set B.
# Each key represents an element, and its value represents
# the corresponding membership degree.
B = {
    "a": 0.4,
    "b": 0.7,
}

# Initialize an empty dictionary to store the fuzzy Cartesian product.
# Each key will be an ordered pair (x, y), and each value will be
# the membership degree of that pair.
cartesian_product = {}

# Generate the Cartesian product of fuzzy sets A and B.
# The membership degree of each ordered pair is calculated using
# the minimum of the membership degrees of its individual elements.
for x, membership_A in A.items():
    for y, membership_B in B.items():
        pair_membership = min(membership_A, membership_B)
        cartesian_product[(x, y)] = pair_membership

# Display the resulting fuzzy Cartesian product.
print("Fuzzy Cartesian Product:")

for pair, membership in cartesian_product.items():
    print(f"{pair}: {membership}")

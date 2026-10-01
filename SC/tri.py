import numpy as np
import matplotlib.pyplot as plt


def triangular_mf(x, a, b, c):
    """
    Calculate the membership value of x in a triangular fuzzy set.

    Parameters:
        x (float): Input value.
        a (float): Left boundary, where membership is 0.
        b (float): Peak, where membership is 1.
        c (float): Right boundary, where membership is 0.

    Returns:
        float: Membership value between 0.0 and 1.0.
    """
    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)


# Define the triangular fuzzy set parameters
a, b, c = 2, 6, 8

# Generate x-values for the plot
x_values = np.linspace(a - 1, c + 1, 500)

# Calculate membership values
membership_values = [
    triangular_mf(x, a, b, c)
    for x in x_values
]

# Calculate the membership value for the example input
x_value = 5
membership = triangular_mf(x_value, a, b, c)

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(
    x_values,
    membership_values,
    label=f"Triangular MF ({a}, {b}, {c})",
    color="blue",
    linewidth=2,
)

# Mark the example point
plt.scatter(
    x_value,
    membership,
    color="red",
    zorder=5,
    label=f"x = {x_value}, μ(x) = {membership:.2f}",
)

# Add labels and formatting
plt.title("Triangular Membership Function")
plt.xlabel("Input value (x)")
plt.ylabel("Membership value μ(x)")
plt.ylim(-0.05, 1.1)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Save the plot locally
file_name = "triangular_membership_function.png"
plt.savefig(file_name, dpi=300, bbox_inches="tight")

# Display the plot
plt.show()

print(f"Membership value at x = {x_value}: {membership}")
print(f"Plot saved as: {file_name}")

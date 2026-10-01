from fractions import Fraction

A = {"1": 0.2, "2": 0.7, "3": 0.5, "4": 0.9}
B = {"1": 0.6, "2": 0.4, "3": 0.8, "4": 0.3}


union = {key: max(A[key], B[key]) for key in A}
"""
This is a dictionary comprehension that creates a new dictionary (union) by iterating over the keys of A and computing the maximum membership value for each key from dictionaries A and B.
"""

intersection = {key: min(A[key], B[key]) for key in A}
complimentOfA = {key: 1 - A[key] for key in A}

def to_fraction(value):
    return Fraction(value).limit_denominator()

print("Set A are: ")
for value in A:
    print(to_fraction(A[value]))

print("===================================================================================================")

print("Set B are: ")
for value in B:
    print(to_fraction(A[value]))


print("===================================================================================================")


print("Union are :")


for value in union:
    print(to_fraction(union[value]))

print("===================================================================================================")


print("Union are :")


for value in intersection:
    print(to_fraction(intersection[value]))



print("===================================================================================================")


print("Compliment of A are :")


for value in union:
    print(to_fraction(complimentOfA[value]))

# Task 1: Arithmetic Operators Practice

# Step 1: Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Perform arithmetic operations and print results

# Addition
addition = num1 + num2
print(f"Addition: {num1} + {num2} = {addition}")

# Subtraction
subtraction = num1 - num2
print(f"Subtraction: {num1} - {num2} = {subtraction}")

# Multiplication
multiplication = num1 * num2
print(f"Multiplication: {num1} * {num2} = {multiplication}")

# Division
division = num1 / num2
print(f"Division: {num1} / {num2} = {division}")

# Division (Handles ZeroDivisionError)
if num2 != 0:
    z_division = num1 / num2
    print(f"Division: {num1} / {num2} = {z_division}")
else:
    print("Division: Cannot divide by zero.")

# Floor Division
floor_division = num1 // num2
print(f"Floor Division: {num1} // {num2} = {floor_division}")

# Floor Division (Handles ZeroDivisionError)
if num2 != 0:
    z_floor_division = num1 // num2
    print(f"Floor Division: {num1} // {num2} = {z_floor_division}")
else:
    print("Floor Division: Cannot divide by zero.")

# Modulus
modulus = num1 % num2
print(f"Modulus: {num1} % {num2} = {modulus}")

# Modulus (Handles ZeroDivisionError)
if num2 != 0:
    modulus = num1 % num2
    print(f"Modulus: {num1} % {num2} = {modulus}")
else:
    print("Modulus: Cannot divide by zero.")

# Exponentiation
exponentiation = num1 ** num2
print(f"Exponentiation: {num1} ** {num2} = {exponentiation}")


# Task 2: Assignment Operators Exploration

# Step 1: Initialize the variable `x` with the value 10
x = 10
print(f"Initial value of x: {x}")

# Step 2: Using shorthand assignment operators to update `x`

# Add 5 to `x`
x += 5
print(f"After adding 5, x = {x}")

# Subtract 2 from `x`
x -= 2
print(f"After subtracting 2, x = {x}")

# Multiply `x` by 3
x *= 3
print(f"After multiplying by 3, x = {x}")

# Divide `x` by 4
x /= 4
print(f"After dividing by 4, x = {x}")

# Perform floor division of `x` by 2
x //= 2
print(f"After floor dividing by 2, x = {x}")

# Take modulus 3 of `x`
x %= 3
print(f"After modulus 3, x = {x}")

# Raise `x` to the power of 2
x **= 2
print(f"After raising to the power of 2, x = {x}")


# Task 3: Comparison Operators

# Step 1: Accept two floating-point numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Compare the two numbers using comparison operators and print the results

# Equal to (==)
print(f"{num1} == {num2}: {num1 == num2}")

# Not equal to (!=)
print(f"{num1} != {num2}: {num1 != num2}")

# Greater than (>)
print(f"{num1} > {num2}: {num1 > num2}")

# Less than (<)
print(f"{num1} < {num2}: {num1 < num2}")

# Greater than or equal to (>=)
print(f"{num1} >= {num2}: {num1 >= num2}")

# Less than or equal to (<=)
print(f"{num1} <= {num2}: {num1 <= num2}")


# Task 4: Logical Operators

# Step 1: Ask the user for two boolean inputs (True or False)
condition1 = bool(int(input("Enter 1 for True or 0 for False (Condition 1): ")))
condition2 = bool(int(input("Enter 1 for True or 0 for False (Condition 2): ")))

# Step 2: Using logical operators to evaluate the conditions

# All two conditions are true (and)
all_true = condition1 and condition2
print(f"Both conditions are true: {all_true}")

# At least one condition is true (or)
at_least_one_true = condition1 or condition2
print(f"At least one condition is true: {at_least_one_true}")

# The opposite of the first condition (not)
opposite_of_first = not condition1
print(f"The opposite of the first condition: {opposite_of_first}")


# Task 5: Identity Operators Exploration

# Step 1: Create two variables `a` and `b`, both containing the same list.
a = [1, 2, 3]
b = a  # `b` references the same list as `a`

# Step 2: Create another variable `c` with a different list but the same elements as `a`.
c = [1, 2, 3]  # `c` is a different list with the same elements

# Step 3: Use identity operators to compare `a`, `b`, and `c`

# `is` checks if two variables point to the same object
print(f"a is b: {a is b}")  # True because `a` and `b` reference the same list
print(f"a is c: {a is c}")  # False because `a` and `c` are different objects

# `is not` checks if two variables point to different objects
print(f"a is not c: {a is not c}")  # True because `a` and `c` are not the same object
print(f"b is not c: {b is not c}")  # True because `b` and `c` are different objects


# Task 6: Membership Operators with Sequences

# Step 1: Create a list of favorite foods (minimum 5 items)
favorite_foods = ["pizza", "burger", "briyani", "chicken rice", "noodles"]


# Step 2: Ask the user to input a food item
food_input = input("Enter a food item: ").lower()

# Step 3: Check if the entered food is in the list using 'in' operator
print(f"Is {food_input.upper()} in your list of favorite foods?",food_input in favorite_foods)

# Step 4: Use 'not in' to check if 'pizza' is not in the list
print(f"Is {food_input.upper()} not in your list of favorite foods?",food_input not in favorite_foods)





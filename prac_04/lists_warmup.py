# Sample list of numbers
digits = [3, 1, 4, 1, 5, 9, 2]

# Q&A style breakdown (answers kept for clarity):
# digits[0] → 3
# digits[-1] → 2
# digits[3] → 1
# digits[:-1] → [3, 1, 4, 1, 5, 9]
# digits[3:4] → [1]
# 5 in digits → True
# 7 in digits → False
# "3" in digits → False (string vs int)
# digits + [6, 5, 3] → [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Modifying the list:
digits[0] = "ten"   # Change first element to string "ten"
digits[-1] = 1      # Change last element to integer 1

# Print from the third element onward
print(digits[2:])

# Check if number 9 exists in the list
print(9 in digits)

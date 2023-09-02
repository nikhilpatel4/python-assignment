# Define a function to calculate the area of a square
def area(side_length):
    return side_length ** 2

# Input: Get the length of a side from the user
side_length = float(input("Enter the length of a side of the square: "))

# Calculate the area using the function
area_result = area(side_length)

# Output: Display the area of the square
print(f"The area of the square with side length {side_length} is {area_result}")

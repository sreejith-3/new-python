# Define a string
text = "hello beautiful world"

# Check if the substring from index 0 to 18 ends with 'beautiful world'
result = text.endswith('beautiful world', 0, 21)
print(result)
result1 = text.endswith('beautiful world')

# Output the result
print(result1)  # Output: False

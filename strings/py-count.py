### Syntax : string.count(substring, start, end) # Start Index , End Index
### ======================================================================

# Define a string
text = "hello world, hello universe"

# Count the number of occurrences of 'hello'
count_hello = text.count("hello")

# Output the result
print(count_hello)  # Output: 2

print("=====================================================")

# Define a string
text = "hello world, hello universe"

# Count the number of occurrences of 'hello' between indices 0 and 15
count_hello = text.count("hello", 0, 15)

# Output the result
print(count_hello)  # Output: 1

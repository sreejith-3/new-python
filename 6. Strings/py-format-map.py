### string.format_map(mapping)

# Define a string with placeholders
text = "Hello, {name}!"

# Define a dictionary with the value for the placeholder
mapping = {"name": "Alice"}

# Format the string using format_map
formatted_text = text.format_map(mapping)

# Output the result
print(formatted_text)  # Output: Hello, Alice!

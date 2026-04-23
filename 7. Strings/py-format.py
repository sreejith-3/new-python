### format()	Formats specified values in a string

# Define a string with placeholders
text = "Hello, {}!"

# Format the string with a value
formatted_text = text.format("Alice I am here")

# Output the result
print(formatted_text)  # Output: Hello, Alice!


### Another example

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49)) 
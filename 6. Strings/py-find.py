### find()	Searches the string for a specified value and returns the position of where it was found

### string.find(substring, start, end)

# Define a string
text = "hello world"

# Find the index of the first occurrence of 'world'
index = text.find('hello')
index1 = text.find('world')

# Output the result
print("The index value is", {index})  # Output: 6
print("The index value is" , {index1})

print("The index value is", index)
print("The index value is" , index1)
### Another example

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x) 
print("The index value is" , x)
print("The index value is" , {x})
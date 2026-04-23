### expandtabs()	Sets the tab size of the string
### string.expandtabs(tabsize)

# Define a string with tab characters
text = "hello\tworld"

# Replace tabs with spaces (default tab size 8)
expanded_text = text.expandtabs()

# Output the result
print(f"'{expanded_text}'")


### Another example 

txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2)

print(x)
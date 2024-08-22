
f = open("data-file1.txt" , "a")  # append creates a new file if the file does not exist
f.write("This is the new line\n")
f.write("This is the second line")
f.close()

f = open("data-file1.txt", "r")
print(f.read())
f.close()
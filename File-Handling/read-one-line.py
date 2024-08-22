## Read one line of the file:

f = open("data-file.txt", "r")
print(f.readline()) # reads firt line 
print(f.readline()) # reads second line 

print("============================================")

## Loop through the file line by line:

f = open("data-file.txt", "r")
for x in f:
  print(x)
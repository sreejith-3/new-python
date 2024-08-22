f = open("data-file.txt", "rt")
print(f.read())

## f = open("D:\\myfiles\welcome.txt", "r")
## print(f.read())

### Return the 5 first characters of the file:
f = open("data-file.txt", "r")
print(f.read(5))  # print first 5 characters

f = open("data-file.txt", "r")
print(f.read(20))  # print first 5 characters

## Read one line of the file:

f = open("demofile.txt", "r")
print(f.readline())
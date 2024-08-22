## Close the file when you are finish with it:

f = open("data-file.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()
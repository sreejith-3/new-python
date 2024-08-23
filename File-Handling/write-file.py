f = open("data-file1.txt" , "w")
f.write("The BOSS IS HERE")
f.close

f = open("data-file1.txt" , "r")
print(f.read())
f.close
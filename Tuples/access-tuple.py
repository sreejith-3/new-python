thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

print("========================================")

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

print("========================================")

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

print("========================================")
### This example returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

print("========================================")
### This example returns the items from "cherry" and to the end:
    
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
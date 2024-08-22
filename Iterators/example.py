### Return an iterator from a tuple, and print each value:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

print("========================================")

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print("========================================")

### Iterate the values of a tuple:

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
  
print("========================================")

### Iterate the characters of a string:

mystr = "banana"

for x in mystr:
  print(x)
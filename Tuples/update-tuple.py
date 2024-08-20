x = ("apple", "banana", "cherry")
y = list(x)  # This converts tuple to a list
print(y)
y[1] = "kiwi"
x = tuple(y) # This converts list to a tuple

print(x)

print("==============================================")
### Because Tuple cannot ne edited we are conveting to list , updating it and then converting to Tuple again
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

print("================================================")

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

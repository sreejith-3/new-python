### The try block will generate an exception, because x is not defined:

try:
  # x = 6 -- I added this line this is not there.
  print(x)
except:
  print("An exception occurred")
  
print("====================================")

### Print one message if the try block raises a NameError and another for other errors:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
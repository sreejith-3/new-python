### A variable created inside a function is available inside that function:
def myfunc():
  x = 300
  print(x)

myfunc()

print("==================================================")

### The local variable can be accessed from a function within the function:

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


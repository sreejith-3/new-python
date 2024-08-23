import os
if os.path.exists("data-file1.txt"):
  os.remove("data-file1.txt")
else:
  print("The file does not exist")
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# newarr = arr.reshape(4, 3)

newarr = arr.reshape(6, 2)

print(newarr)

print("=====================================")

### Convert the following 1-D array with 12 elements into a 3-D array.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)
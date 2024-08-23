import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array:', arr.shape)


Output:
    
    [[[[[1 2 3 4]]]]]
shape of array: (1, 1, 1, 1, 4)

How It Becomes 5-Dimensional:

ndmin=5: This argument tells NumPy that the array should have at least 5 dimensions.
The original list [1, 2, 3, 4] is 1-dimensional with a shape of (4,).
To satisfy the ndmin=5 requirement, NumPy adds additional dimensions of size 1, making the shape (1, 1, 1, 1, 4).

Understanding the Shape:
The shape (1, 1, 1, 1, 4) means the array has 5 dimensions:
The first dimension has a size of 1.
The second dimension has a size of 1.
The third dimension has a size of 1.
The fourth dimension has a size of 1.
The fifth dimension has a size of 4, which contains the elements [1, 2, 3, 4].

Visualization:
You can think of the array as being nested within multiple layers of single-element dimensions, like this:

The innermost level has [1, 2, 3, 4].
Each higher level wraps this in another layer of single-element arrays.
In summary: The ndmin=5 argument forces the array to have 5 dimensions, with the first four dimensions having a size of 1, and the last dimension containing the actual data [1, 2, 3, 4].

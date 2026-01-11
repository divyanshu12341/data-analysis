# Loops are discouraged because they are slow in Python at scale,
# whereas optimized libraries execute operations in compiled code
#  outside Python.

# Python loops operate one element at a time
# Large datasets = millions of operations
# Python’s interpreter becomes the bottleneck

# Numpy
# Stores data in contiguous memory
# Executes operations in compiled C code
# Applies operations to entire arrays at once (vectorization)

import numpy as np
data = np.array([10,20,30,40,50])
print(data)
print(type(data))

# data looks like a list but is not a list
# It is a NumPy ndarray
# All elements are the same data type

# Vectorized operation
print(data+5)
print(data+2)

# Mini-exercise
# Create a NumPy array with 5 numbers
# Multiply the entire array by 3
# Print the result
# Paste only your code.


x = np.array([5,7,6,8,11])
ans = x*3
print(ans)

# Using a NumPy array of daily sales:
# Compute total sales
# Compute average sales
# Compute standard deviation

daily_sales = np.array([100,102,101,201,203,202])
sum_sales = daily_sales.sum()
avg_sales = daily_sales.mean()
std_sales = daily_sales.std()
print("Sum is ",sum_sales)
print("Average is ",avg_sales)
print("Standard deviation is ",std_sales)

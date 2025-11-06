import numpy as np

arr1=np.array([10,20,30,40,50,60])
arr4=np.array([5,10,15,20,25,30])
arr2=np.array([[10,20],[30,40]])
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])



print("arr1:",arr1)
print("arr2:",arr2)
print("arr3:",arr3)

reshaped_arr = arr1.reshape((2,3))
print(f"Reshaped array:\n{reshaped_arr}")

transposeed_arr=arr2.T
print(transposeed_arr)

add=arr1+arr4
sub=arr1-arr4

print("addition:",add)
print("substraction:",sub)

element = arr[1, 2]
print(f"Element at (1, 2): {element}")

row_slice = arr[0:2, :]
print(f"Row slice:\n{row_slice}")

col_slice = arr[:, 1]
print(f"Column slice: {col_slice}")

greater_than_5 = arr[arr > 5]
print(f"Elements greater than 5: {greater_than_5}")
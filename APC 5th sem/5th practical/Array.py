import array as arr

arr1=arr.array('i',[10,20,30,40])
arr2=arr.array('i',[5,15,25,35])

arr1.append(50)
arr1.insert(2,25)
arr1.remove(20)
arr1.pop(3)
arr1[2]=30
count = arr1.count(20)
arr1.reverse()

arr1.extend([60,70])
arr3 = arr.array('i',[100,200,300])
# arr1.fromlist([80,90])
# arr1.byteswap()
length = len(arr1)
# index = arr1.index(10)
# buffer = arr1.buffer_info()
# arr4 = arr1.tolist()
# arr1.itemsize
# arr1.tobytes()
# arr1.typecode

print("Here is the list of available arrays:",end="")
print("\narray 1:")
for i in range(0,5):
    print(arr1[i],end=" ")

print("\narray 2:")
for i in range(0,4):
    print(arr2[i],end=" ")

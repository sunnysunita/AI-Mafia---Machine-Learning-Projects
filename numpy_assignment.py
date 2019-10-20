# 1. Import the numpy package under the name  (★☆☆)"
import numpy as np

# 2. Print the numpy version and the configuration  (★☆☆)"
print(np.__version__)

# 3. Create a null vector of size 10 (★☆☆)"
arr = np.zeros(10)
print(arr)

# 4.  How to find the memory size of any array (★☆☆)"
print(len(arr))

# 5.  How to get the documentation of the numpy add function from the command line?
# %run `python -c "import numpy; numpy.info(numpy.add)"`

# 6.  Create a null vector of size 10 but the fifth value which is 1 (★☆☆)"
arr1 = np.zeros(10)
arr1[4] = 1
print(arr1)

# 7.  Create a vector with values ranging from 10 to 49 (★☆☆)"
arr2 = np.arange(10, 50, 1)
print(arr2)
#arr21=np.random.randint(10,50,10)
#print(arr21)

# 8.  Reverse a vector (first element becomes last) (★☆☆)"
arr3 = np.arange(11)
print(arr3)
arr3 = arr3[::-1]
print(arr3)

# 9.  Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)"
mat = np.random.randint(0,8,(3,3))
print(mat)
#mat1=np.arange(0,9,1).reshape(3,3)
#print(mat1)

# 10. Find indices of non-zero elements from \\[1,2,0,0,4,0\\] (★☆☆)"
list=[1,2,0,0,4,0]
arr4=np.array(list)
print(arr4)
for i in range(0,len(arr4)):
    if arr4[i]!=0:
        print(i)

#nz = np.nonzero([1,2,0,0,4,0])
#print(nz)

# 11. Create a 3x3 identity matrix (★☆☆)"
mat2=np.eye(3,3)
print(mat2)

# 12. Create a 3x3x3 array with random values (★☆☆)"
mat3=np.random.random((3,3,3))
print(mat3)

# 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)"
mat4=np.random.random((10,10))
print("max=",np.max(mat4))
print("min=",np.min(mat4))

# 14. Create a random vector of size 30 and find the mean value (★☆☆)"
arr5=np.random.random(30)
print(arr5)
print("mean=",np.mean(arr5))

# 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)"
Z = np.ones((5,5))
Z[1:4,1:4] = 0
print(Z)

# 16. How to add a border (filled with 0's) around an existing array? (★☆☆)"
Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)

# 17. What is the result of the following expression? (★☆☆)"
# nan is (literally) not a number, you can't do arithmetic with it
# inf is infinity - a value that is greater than any other value.
# -inf is therefore smaller than any other value.
print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)

# 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)"
mat5 = np.diag(1+np.arange(4), k=-1)
print(mat5)

# 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)"
mat6=np.zeros((8,8))
print(mat6)
mat6[1::2,::2] = 1
mat6[::2,1::2] = 1
print(mat6)

# 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?"
print(np.unravel_index(99,(6,7,8)))

# 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)"
arr6=np.array([[0,1],
               [1,0]])
print(np.tile(arr6,(4,4)))

# 22. Normalize a 5x5 random matrix (★☆☆)"
mat7=np.random.random((5,5))
mat8=((mat7-np.mean(mat7))/np.std(mat7))
#print(mat7)
print(mat8)

# 23. Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)"
color = np.dtype([("r", np.ubyte, (1,)),
                  ("g", np.ubyte, (1,)),
                  ("b", np.ubyte, (1,)),
                  ("a", np.ubyte, (1,))])
print(color)

# 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)"
mat9=np.arange(0,15,1).reshape(5,3)
mat8=np.arange(0,6,1).reshape(3,2)
print(mat9@mat8)

# 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)"
arr7=np.arange(0,11,1).astype(int)
print(arr7)
cond=np.logical_and(arr7>=3,arr7<=8)
arr7=np.select([~cond,cond],[arr7,-arr7])
print(arr7)

# 26. What is the output of the following script? (★☆☆)"
print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))

# 27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)"
#  Z**Z
#  2 << Z >> 2
#  Z <- Z
#  1j*Z
#  Z/1/1
#  Z<Z>Z

# 28. What are the result of the following expressions?"
# print(np.array(0) / np.array(0))
# print(np.array(0) // np.array(0))
# print(np.array([np.nan]).astype(int).astype(float))

# 29. How to round away from zero a float array ? (★☆☆)"
mat10=np.random.uniform(-10,+10,10)
print(mat10)
# mat10=np.random.uniform(-10,+10,10).astype(int)
# print(mat10.astype(float))
print (np.copysign(np.ceil(np.abs(mat10)), mat10))
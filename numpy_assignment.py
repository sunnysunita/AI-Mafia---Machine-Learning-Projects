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
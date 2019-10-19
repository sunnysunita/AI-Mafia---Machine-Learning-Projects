# 1. Import the numpy package under the name  (★☆☆)"
import numpy as np

# 2. Print the numpy version and the configuration  (★☆☆)"
print(np.__version__)

# 3. Create a null vector of size 10 (★☆☆)"
arr=np.zeros(10)
print(arr)

# 4.  How to find the memory size of any array (★☆☆)"
print(len(arr))

# 5.  How to get the documentation of the numpy add function from the command line?
# %run `python -c "import numpy; numpy.info(numpy.add)"`

# 6.  Create a null vector of size 10 but the fifth value which is 1 (★☆☆)"
arr1=np.zeros(10)
arr1[4]=1
print(arr1)

# 7.  Create a vector with values ranging from 10 to 49 (★☆☆)"
arr2=np.arange(10,50,1)
print(arr2)

# 8.  Reverse a vector (first element becomes last) (★☆☆)"
arr3 = np.arange(11)
arr3 = arr3[::-1]
print(arr3)
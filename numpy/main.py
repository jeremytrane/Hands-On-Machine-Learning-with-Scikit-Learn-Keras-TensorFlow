## Intro to Numpy

import numpy as np

# print numpy version
# print(np.__version__)

array = np.array([1, 2, 3, 4])

# my_list = [1, 2, 3, 4]
# print(my_list)

# print(array)
# print(type(array))

array = array * 2

#  #print(array)

## Multidimensional Array

import numpy as np

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])
# print(array.ndim)
# print(array.shape)
# print(array[0, 0, 1])

word = array[0, 0, 0]  + array[2, 0, 0]  + array[2, 0, 0]
# print(word)

# Slicing

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14,15, 16],])

# array[start:end:step]

# print(array[0:3:2])
# print(array[:, 0])

# Arethmetic

# scalar
array = np.array([1, 2, 3])

# print(array + 1)
# print(array - 2)
# print(array * 3)
# print(array / 4)
# print(array ** 5)

# vectorized math funcs

array = np.array([1.01, 2.5, 3.99])

# print(np.sqrt(array))
# print(np.ceil(array))

# print(array == 2.5)

array[array < 2] = 0
# print(array)

# Broadcasting
array1 = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])
array2 = np.array([[1], [2], [3], [4]])

# print(array1.shape)
# print(array2.shape)

# print(array1+array2)

# Aggregate function

array = np.array([[1, 2 , 3, 4 , 5], [6, 7 , 8 , 9 , 10]])
# print(np.sum(array))
# print(np.mean(array))
# print(np.std(array))
# print(np.var(array)) # var is sqr of std
# print(np.min(array))
# print(np.max(array))
# print(np.argmin(array))
# print(np.argmax(array))
# print(np.sum(array, axis=0)) # summing all columns
# print(np.sum(array, axis=1)) # summing all rows

# Filtering

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])


children = ages[ages < 18]
# print(children)
adults = np.where(ages >= 18, ages, 0) # Do this if you need to preserve original array, (condition, array, fillter number)

# print(adults)

# Random Numbers

rng = np.random.default_rng()

# print(rng.integers(low=1, high=101, size=(3,2))) # second number is exclusive

np.random.seed(seed=1)
print(np.random.uniform(low=-1, high=1, size=3))

array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)

# use rng.choice for list
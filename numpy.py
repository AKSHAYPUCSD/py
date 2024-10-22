import array
import numpy as np

L = list(range(10))
L 
[0,1,2,3,4,5,6,7,8,9]
print(L)
print(type(L[0]))                        #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                                         #<class 'int'>

L3 = [True, "2",3.0,4]
print(L3)                             
print([type(item) for item in L3])       # [True, '2', 3.0, 4]
                                         # [<class 'bool'>, <class 'str'>, <class 'float'>, <class 'int'>] 

L4 = list(range(10))
A = array.array('i',L4)
print(A)                                # array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# np.array([1,4,2,5,3])
# print(type(np.array))

# array([1,4,2,5,3])
# print(type(array))

# np.ones((3,5),dtype=float)
# print(np.ones)

#NumPy arrays Manipulation
#1) Data Manipulation
#2) Attributes of Arrays
#3)Slicing Of Arrays

x1 = np.random.randint(10,size=6)
print(x1)
                         
x2 = np.random.randint(10,size=(3,4)) #Two Dimentional
print(x2)                        

x3 = np.random.randint(10,size=(3,4,5)) # Three Dimensional
print(x3)
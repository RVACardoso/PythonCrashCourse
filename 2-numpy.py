import numpy as np

# short numpy intro
a = [1,2,3,4,5,6,7,8,9]
A = np.array(a)
print("\n Array A:\n {}".format(A))

line1 = [1,2,3]
line2 = [4,5,6]
B = np.array([line1, line2])
print("\n Array B:\n {}".format(B))

spaced = np.arange(2,29,3) #includes first, not last
print("\n Equally spaced:\n {}".format(spaced))

print("\n 0 filled matrices: ")
zero = np.zeros((2,3))
print(zero)
print("\n 1 filled matrices: ")
one = np.ones((3,3))
print(one)

print("\n Identity matrices: ")
ident = np.eye(3)
print(ident)

print("\n Multiply matrices: ")
M = np.dot(one, ident)
print(M)

print("\n Get shape")
print(M.shape)

print("\n Reshape Array: ")
Res = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9] )
print(Res)
Res = Res.reshape(3,3)
print(Res)


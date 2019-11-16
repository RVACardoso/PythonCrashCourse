import numpy as np

# short numpy intro
a = [1,2,3,4,5,6,7,8,9]
A = np.array(a)
print("\n Array A:\n {}".format(A))

line1 = [1,2,3]
line2 = [4,5,6]
mat_list = [line1, line2]
B = np.array(mat_list)
print("\n Array B:\n {}".format(B))

spaced1 = np.arange(2,29,3) #includes first, not last
print("\n Equally spaced given spacing:\n {}".format(spaced1))

spaced2 = np.linspace(2,29,13) #includes first and last
print("\n Equally spaced given spacing:\n {}".format(spaced2))

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
Res = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(Res)
Res = Res.reshape(3,3)
print(Res)


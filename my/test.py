import numpy as np

a = np.mgrid[0:9, 0:6]
# b = np.mgrid[0:3, 0:3]
# b = np.meshgrid[0:4, 0:4]

# print(a)
#
# a = a.T.reshape(-1, 2)
# print(a)

objp = np.zeros((9 * 6, 3), np.float32)
print(objp)
print(objp.shape)
objp[0:54, 0:2] = a.T.reshape(-1, 2)
# print(objp[0:54, 0:3])

# a = a.flatten(order='F')
# print(a)
# print(len(a))

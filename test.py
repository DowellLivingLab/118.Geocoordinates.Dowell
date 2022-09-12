# from ctypes import *
# c_file = "D:/fiverr/dowell/test.so"
# c_fun = CDLL(c_file, mode=RTLD_GLOBAL)

# a = float(input("Input Radius: "))
# b = int(input("Input Length: "))
# c = int(input("Input Width: "))

# result = c_fun.inscribe(a, b, c)
# print("\nTotal Circles:  ", result)



from setuptools import setup, Extension

# Compile *mysum.cpp* into a shared library
setup(
    #...
    ext_modules=[Extension('algorithm', ['algorithm.cpp'],),],
)




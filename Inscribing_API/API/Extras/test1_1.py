
import ctypes
import glob

# find the shared library, the path depends on the platform and Python version
libfile = glob.glob('build/*/algorithm*.so')[0]

# 1. open the shared library
mylib = ctypes.CDLL(libfile)

mylib.inscribe.restype = ctypes.c_int
mylib.inscribe.argtypes = [ctypes.c_float, ctypes.c_int, ctypes.c_int]

result = mylib.inscribe(0.1, 5000, 5000)
print(result)

import ctypes
from ctypes import c_char_p

# Load DLL (adjust path to your .dll)
engine = ctypes.CDLL('./build/Release/engine.dll')

# Set argument and return types
engine.process_input.argtypes = [c_char_p]
engine.process_input.restype = c_char_p

# Call C function
input_str = "Hello from Python"
result = engine.process_input(input_str.encode('utf-8')).decode('utf-8')

# Decode and print result
print(result)
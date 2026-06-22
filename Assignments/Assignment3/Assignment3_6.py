# ----------------------------------------------------------------------
# Author    : Shraddha Dhananjay Mutange
# Data      : 22/06/2026
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Problem : Write a program to display :
#           - Data type
#           - Memory address
#           - Size in bytes
#           of a variable entered by the user.
# ----------------------------------------------------------------------

import sys

Value = input("Enter a value : ")

print("Data type of value : ", type(Value))
print("Memory address of value : ", id(Value))
print("Size of value : ", sys.getsizeof(Value), "bytes")

# ----------------------------------------------------------------------
# ----------------------------- OUTPUT ---------------------------------
# ----------------------------------------------------------------------
# 
# Enter a value : 11
# Data type of value :  <class 'str'>
# Memory address of value :  129235777043552
# Size of value :  43 bytes
# 
# 
# Enter a value : Shraddha
# Data type of value :  <class 'str'>
# Memory address of value :  130353465556528
# Size of value :  49 bytes
# 
# ----------------------------------------------------------------------
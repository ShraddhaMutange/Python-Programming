# Author    : Shraddha Dhananjay Mutange
# Date      : 15/06/2026

# Problem : Whats the difference between
#           a = 10, b = 10
#           and
#           a = [10], b = [10]
#           Explain using id().

a = 10
b = 10

print("Type of a = 10 is :", type(a))
print("Memory Address of a = 10 is :", id(a))
print("Type of b = 10 is :", type(b))
print("Memory Address of b = 10 is :", id(b))

a = [10]
b = [10]

print("Type of a = [10] is :", type(a))
print("Memory Address of a = [10] is :", id(a))
print("Type of b = [10] is :", type(b))
print("Memory Address of b = [10] is :", id(b))

# -------------------------------------------------------------
# -------------------------Output------------------------------
# -------------------------------------------------------------
# 
# Type of a = 10 is : <class 'int'>
# Memory Address of a = 10 is : 11755976
# Type of b = 10 is : <class 'int'>
# Memory Address of b = 10 is : 11755976
# 
# Type of a = [10] is : <class 'list'>
# Memory Address of a = [10] is : 130406088887104
# Type of b = [10] is : <class 'list'>
# Memory Address of b = [10] is : 130406088888896
# 
# -------------------------------------------------------------
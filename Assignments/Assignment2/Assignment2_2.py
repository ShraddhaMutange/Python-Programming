# Problem : What is the difference between:
#           a = 10
#           b = 10
#           and
#           a = [10]
#           b = [10]
#           Explain using id().

a = 10
b = 10

print("Type of a=10 is : ", type(a))
print("ID of a=10 is : ", id(a))
print("Type of b=10 is : ", type(b))
print("ID of b=10 is : ", id(b))

a = [10]
b = [10]

print("Type of a=[10] is : ", type(a))
print("ID of a=[10] is : ", id(a))
print("Type of b=[10] is : ", type(b))
print("ID of b=[10] is : ", id(b))

# -----------------------------------------------------------------------
# ---------------------------------Output--------------------------------
# -----------------------------------------------------------------------
# 
# Type of a=10 is :  <class 'int'>
# ID of a=10 is :  11755976
# Type of b=10 is :  <class 'int'>
# ID of b=10 is :  11755976
# Type of a=[10] is :  <class 'list'>
# ID of a=[10] is :  139350784002880
# Type of b=[10] is :  <class 'list'>
# ID of b=[10] is :  139350784004672
# 
# -----------------------------------------------------------------------
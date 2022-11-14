# Comparisons to singletons like None should always
# be don with "is" or "is not"
# x = [1, 2]
#
# if x is not None:
#     print("hi")


# Always use def statement instead of an assignment
# statement that binds a lambda expression
import math


def f(x): return 2 * x


print(f(5))

# Avoid using a bare except: statement

# try:
#     a = int("hi")
# except ImportError:
#     print("Error")


# If a function returns an expression, you should add
# return None statement

# def do_sqrt(x):
#     if x >= 0:
#         return math.sqrt(x)
#     else:
#         return None
#
#
# def bar(x):
#     if x < 0:
#         return None
#     return math.sqrt(x)


# Use ''.startswith() and ''.endswith() instead of string
# slicing to check for prefixes or suffixes

car = 'autoinsurance'

# print(car[-4:])

# if car.startswith('auto'):
#     print("Correct")
# else:
#     print("Incorrect")

# Object type comparisons should always use
# isinstance() instead of comparing types directly:

number = 45
#
# if isinstance(number, int):
#     print("Correct")

# Don’t compare boolean values to True or
# False using ==:
bool_ = True

if not bool_:
    print("hi")



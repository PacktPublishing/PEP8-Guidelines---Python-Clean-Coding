
import copy,code,codecs,csv,ctypes,random,codeop,email,datetime,decimal,\
    dbm,distutils,genericpath




# 1. Braking inputs line in 8 spaces (2 tabs) for the beginning of the line
# 2. Breaking inputs line only from a bracket
# 3. Every next break is from a comma
def long_function(
        variable_one, variable_two,
        variable_three, variable_four):
    print("Hi PEP8")


variable_one, variable_two, variable_three, variable_four = 1, 2, 3, 4

person = long_function(variable_one, variable_two,
                       variable_three, variable_four)

clean = True
available = True

# The if statement checks if we can sell a house, based on clean and available attributes.
if clean and \
        available:
    print('Ready for viewing')

even_numbers = [
    2, 4, 6, 8, 10,
    12, 14, 16, 18,
    20,
]


def my_func(a, b, c, d, e, f):
    print(a, b, c, d, e, f)


my_func(
    'a', 'b', 'c',
    'd', 'e', 'f',
)

# Lorem Ipsum is simply dummy text of the printing and typesetting industry.
# Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
# when an unknown printer took a galley of type and scrambled it to make a
# type specimen book. It has survived not only five centuries, but also the
# leap into electronic typesetting, remaining essentially unchanged. It was
# popularised in the 1960s with the release of Letraset sheets containing
# Lorem Ipsum passages, and more recently with desktop publishing software
# like Aldus PageMaker including versions of Lorem Ipsum.

hello_everyone_how_are_you_are_you_ok_i_am_good= 1
hello_everyone_how_are_you_are_you_ok_i_am_good1 = 2

if hello_everyone_how_are_you_are_you_ok_i_am_good1 == 2 or\
        hello_everyone_how_are_you_are_you_ok_i_am_good == 1:
    pass

with open('path/to/some/file/you/want/to/read') as file1, \
     open('/path/tosome/file/being/written', 'w') as file2:
    file2.write(file1.read())

# Python code to demonstrate
# decode()


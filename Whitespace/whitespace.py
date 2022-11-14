'''
Always surround these binary operators with a single space on either side:
assignment (=), augmented assignment (+=, -= etc.), comparisons
(==, <, >, !=, <>, <=, >=, in, not in, is, is not), Booleans (and, or, not).
If operators with different priorities are used, consider adding whitespace
around the operators with the lowest priority(ies).
'''

i = 0
while i < 5:
    print("hi")
    i = i + 1
    i += 1

x = 1
x = x * 2 - 1
y = 2

result = x * x + y * y
c = (x + y) * (x - y)

# Functions

str1 = "hello"


def merge(input: str1):
    print(str1)


def retstr(str2) -> str:
    return str2


def img(image, pixels=1000):
    return image, pixels


print(img(5, 500))

if str1 == "hello":
    print("python")


def do_one():
    pass


def do_two():
    pass


def do_three(a, b, c):
    return a, b, c


do_one()
do_two()
do_three()

try:
    print(5)
finally:
    print(6)

do_one()
do_two()
do_three(
    "hahahha", "hi all", "python")

mytuple = ("apple",)

FILES = [
    "config.py",
    "pytest.ini",
]


def use_files(files, error):
    if error:
        print(files[0], "and", files[1], "Should not be imported")
    else:
        print("All files are okay")


use_files(FILES,
          error=True,
          )


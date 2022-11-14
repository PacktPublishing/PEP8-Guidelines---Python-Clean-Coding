class Person:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight


    def get_data(self):
        # Printing height and weight of a person
        print("Height: ", self.height, "Weight: ", self.weight)

        # Checking height
        if self.height > 6:
            print("Too tall")
        elif self.height < 5:
            print("Too short")
        else:
            print("Perfect")

alpha = 1
# adam = Person(5.5, 150)
# adam.get_data()

# Encoding
# Python distribution should always use UTF-8
print(('刀女').encode("unicode_escape"))
print(len('刀女'.encode()))

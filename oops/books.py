class MotorBike:
    def __init__(self, gear, speed):
        self.gear = gear
        self.speed = speed

    def __repr__(self):
        return repr((self.gear, self.speed))


bike1 = MotorBike(5, 100)
print(bike1)


class Book:
    def __init__(self, name, no_of_copies):
        self.name = name
        self.no_of_copies = no_of_copies

    def __repr__(self):
        return repr((self.name, self.no_of_copies))

    def increase_no_of_copies(self, how_much):
        self.no_of_copies += how_much

    def decrease_no_of_copies(self, how_much):
        self.no_of_copies -= how_much


book1 = Book('Mastering Spring 5.0', 12)
book2 = Book('Mastering Python', 23)

print(book1)
print(book2)

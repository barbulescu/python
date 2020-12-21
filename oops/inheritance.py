class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return repr(self.name)


class Student(Person):
    def __init__(self, name, college_name):
        super().__init__(name)
        self.college_name = college_name

    def __repr__(self):
        return repr((super().__repr__(), self.college_name))


person = Person('Marius')
print(person)
student = Student('Marius', 'Politehnica Timisoara')
print(student)

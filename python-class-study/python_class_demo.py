class Person:
    def __init__(self, name=None, __age=None):
        self.name = name
        self.__age = __age

    def update_name(self, name):
        self.name = name

    def print_object(self):
        print("person name %s" % self.name)


p1 = Person('stupid')
p1.print_object()
p1.name = '123'
p1.print_object()



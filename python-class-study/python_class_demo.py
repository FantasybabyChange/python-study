class Person:
    __hp = 10

    def __init__(self, name=None, __age=None):
        self.name = name
        self.__age = __age

    def update_name(self, name):
        self.name = name

    def print_object(self):
        print("person name %s hp %s " % (self.name, self.__hp))

    def update_hp(self, hp):
        self.__hp = hp


p1 = Person('stupid')
p2 = Person('clear')
p1.print_object()
p1.name = '123'
p1.update_hp(3)
p1._Person__hp = 15
p1.print_object()
p2.print_object()

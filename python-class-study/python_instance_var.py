class Person:
    # 该类属性会被共享
    child = []
    # 该属性不会被共享
    __hp = 3

    def __init__(self, name=None, __age=None):
        self.name = name
        self.__age = __age

    def append_child(self, child):
        self.child.append(child)

    def update_hp(self, hp):
        self.__hp = hp

    def print_object(self):
        print("person name %s child %s hp %s " % (self.name, self.child, self.__hp))


p1 = Person('stupid')
p2 = Person('clear')
p1.print_object()
p1.name = '123'
p1.append_child("x1")
p1.update_hp(10)
# p2.append_child("x2")
p1.print_object()
p2.print_object()

# 类的继承
class Person:
    def __init__(self, name=None, age=None, hp=None):
        self.name = name
        self.__age = age
        self.__hp = hp

    def update_name(self, name):
        self.name = name

    def print_object(self):
        print("person name %s hp %s " % (self.name, self.__hp))

    def get_age(self):
        return self.__age

    def get_hp(self):
        return self.__hp

    def update_hp(self, hp):
        self.__hp = hp


class Boy(Person):
    def __init__(self, name=None, age=None, hp=None):
        super().__init__(name, age, hp)

    def print_object(self):
        print("Boy name %s age %s hp %s " % (self.name, self.get_age(), self.get_hp()))


boy = Boy('小屁孩', 13, 30)
boy.print_object()
boy.update_name('xiao ihai')

person = Person('大人', 30, 100)
person.print_object()

print(type(boy))

print(isinstance(boy, Person))

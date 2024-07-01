class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name
        return self

    def set_age(self, age):
        self.__age = age
        return self

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name


p1 = Person('Aravindh', 23)
print(p1.get_name())
print(p1.get_age())

p1.set_name('Sandy').set_age(41) # This is the use of returning the self. So we can chain the methods.

print(p1.get_name())
print(p1.get_age())

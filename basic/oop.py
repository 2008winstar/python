class Person:
    def __init__(self, name):
        self.name = name
        # self.__class__指向当前类，可以通过它来引用类变量/方法

    def say_hi(self):
        print('Hello, my name is ', self.name)

p = Person('winstar')
p.say_hi()


class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(SchoolMember):
    """继承示例"""
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary











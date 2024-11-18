# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#     @abstractmethod
#     def Sound(self):
#         pass
#
#
# class DOG(Animal):
#
#     def Sound(self):
#         print("sound is bow bow")
#
#
# ob = DOG()
# print(ob.Sound())
#
#
# # Inheritance
# # single Inheritance
#
# class Parent:
#
#     def __init__(self, name, Id):
#         self.name = name
#         self.Id = Id
#
#     def Display(self):
#         print(f"name is {self.name}")
#         print(f"id is {self.Id}")
#
#
# p_ob = Parent("Deepika", 29)
# print(p_ob.Display())
#
#
# class Emp(Parent):
#
#     def Print(self):
#         print("child class is called i.e Emp class")
#
#
# Emp_ob = Emp("Nani", 30)
# print(Emp_ob.Display())
# print(Emp_ob.Print())


# multiple inheritsnce

class Emp_details:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"name is {self.name} and {self.age}")


class Emp_info:
    def __init__(self, id):
        self.id = id

    def show(self):
        print(f"emp id is {self.id}")


class Employee(Emp_details, Emp_info):

    def __init__(self, name, age, id):
        # Emp_details.__init__(self,name, age)
        super().__init__(name, age)
        Emp_info.__init__(self, id)

    def Printer(self):
        print(f"employye deatils inherited")


child_obj = Employee("deepika", 29, 30011827)
print(child_obj.display())
print(child_obj.show())
print(child_obj.Printer())


# Multi level inheritance

class GrandFather:
    def __init__(self, name, age, gf_profession):
        self.name = name
        self.age = age
        self.gf_profession = gf_profession

    def grandfather_details(self):
        print(f"grand father name {self.name} and {self.age}")

    def profession(self):
        print(f"grandfather profession {self.gf_profession}")


class Father(GrandFather):

    def __init__(self, name, age, gf_profession, father_name, f_profession):
        super().__init__(name, age, gf_profession)
        self.father_name = father_name
        self.f_profession = f_profession

    def profession(self):
        print(f"father profession {self.f_profession}")

    def father_details(self):
        print(f"father name is {self.father_name}")


class Son(Father):

    def __init__(self, name, age, gf_profession,  father_name, f_profession, son_name, son_profession):
        super().__init__(name, age, gf_profession,  father_name, f_profession)
        self.son_name = son_name
        self.son_profession = son_profession

    def profession(self):
        print(f"son profession {self.son_profession}")

    def son_details(self):
        print(f"son name is {self.son_name}")


son_obj = Son("allu aravind", 70, "producer", "allu arjun", "hero", "allu ayaan", "student")
son_obj.son_details()
son_obj.father_details()
son_obj.grandfather_details()
son_obj.profession()


# mehtod overloading



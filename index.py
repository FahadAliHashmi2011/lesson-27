from abc import ABC,abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("passed value is:",x)
    @abstractmethod
    def task(self):
            print("we are in a abstract class")
class test_class(Absclass):
     def task (self):
         print("we are inside the test_class task")

test_obj=test_class()
test_obj.task ()
test_obj.print(100)
##############################################################################################
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")
class Snake(Animal):
     def move(self):
          print("i can crawl")
class dog(Animal):
     def move(self):
          print("i can bark")
class lion(Animal):
     def move(self):
          print("i can roar")
r = Human()
r.move()
k=Snake()
k.move()
r=dog()
r.move()
k=lion()
k.move()
##############################################################################################
class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")
    def type(self):
         print("usa is a developed country")

obj_ind =India()
obj_usa =USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
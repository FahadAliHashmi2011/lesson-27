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
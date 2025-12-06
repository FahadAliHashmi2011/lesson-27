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

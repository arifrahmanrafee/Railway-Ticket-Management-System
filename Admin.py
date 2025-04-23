from abc import ABC, abstractmethod
from typing import *

class Admin(ABC):
    """This is the Admin class where the observer will be notified"""
    @abstractmethod
    def add_passanger():
        pass;
    @abstractmethod
    def remove_passanger():
        pass
    @abstractmethod
    def notify():
        pass

class Passanger(ABC):
    @abstractmethod 
    def update(self,Admin:Admin,message):
        pass;

#Concrete class 


class Concrete_staff(Passanger):
    def update(self,Admin:Admin,message):
        print(" Dear Staffs",message);
class Concrete_passanger(Passanger):  
    def update(self,Admin:Admin,message):
        print(" Dear Valued passangers",message)


class Concrete_Admin(Admin):
    _passanger:List[Passanger]=[]
    _name: int=None;
    
    def add_passanger(self,passanger:Passanger):
        self._passanger.append(passanger)
        
    def remove_passanger(self,passanger:Passanger):
        self._passanger.remove(passanger)
        
    def notify(self,message):
        for ob in self._passanger:
            ob.update(self,message);
        
        

    def businesslogic(self,updation_text):
        self.notify(updation_text)








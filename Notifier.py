from abc import ABC,abstractmethod
from Admin import *
class Notification(ABC):
    @abstractmethod
    def send(self, message: str,n:Concrete_passanger):
        pass

class SMS(Notification):
    def send(self, message: str,n:Concrete_passanger):
        print("The SMS is Sent")
        n.businesslogic(message)

class Email(Notification):
    def send(self, message: str,n:Concrete_passanger):
        print("Email is sent")
        n.businesslogic(message)
        

class NotificationFactory:
    @staticmethod
    def create(notifier_type: str) -> Notification:
        if notifier_type == "sms":
            return SMS()
        elif notifier_type == "email":
            return Email()
        else:
            print("Invalid request")

class Factory_passanger_staff:
    def get_instance(self,msg)-> Passanger:
        if msg.lower()=="passanger":
            return Concrete_passanger();
        elif msg.lower()=="staff":
            return Concrete_staff()
        else: 
            raise ValueError("Invalid argument")





subs_1=Factory_passanger_staff().get_instance("passanger");
subs_3=Factory_passanger_staff().get_instance("passanger");
subs_2=Factory_passanger_staff().get_instance("Staff")
chn=Concrete_Admin();
chn.add_passanger(subs_1)
chn.add_passanger(subs_3)
chn.add_passanger(subs_2)


notifier = NotificationFactory.create("email").send("hi there ",chn)  
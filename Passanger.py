import sys
from Train_route import *
from Decorator import * 
from inputs import *
class Passanger_list:
    def __init__(self, name: str, age: int,no_of_tickets:int, email: str, phone: str):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.no_of_tickets=no_of_tickets
        self.booking_history = []
        

    def view_train(self,source,destination,time1,time2)-> train_time:
        return train_time(source,destination,time1,time2).desired_train
    
    def add_booking(self,list_of_train,timing)-> list:
        for li in list_of_train:
            if li.time==str(timing):
                self.booking_history.append(self.name)
                self.booking_history.append(self.age)
                self.booking_history.append(self.email)
                self.booking_history.append(self.phone)
                self.booking_history.append(li.train_name)
                self.booking_history.append(li.source)
                self.booking_history.append(li.destination)
                self.booking_history.append(self.no_of_tickets)
                self.booking_history.append("___________")
        return self.booking_history    
    def extra_service(self,t:Ticket)-> str:
        return t.get_price()+"  "+ t.get_description()




y=Passanger_list("karim",20,5,"krahin@gmailcom","01865757271")
k=y.view_train("Dhaka","Khulna",1600,2100)
if k==[]:
    print("Re start your filter there is no such train")
    sys.exit()
timing=input("enter the preferred timing ")



service= input("enter your service type: Basic, VIP, Extra Meal")
k=y.add_booking(k,timing)
print(k)
t1 = BasicTicket()
t2 = VIPService(t1)
t3 = ExtraBaggage(t2)
t4 = MealOption(t3)
if service=="Basic":
    print(t1.get_description(), t1.get_price())
if service=="VIP":
    print(t2.get_description(),t2.get_price())
if service=="Extra":
    print(t3.get_description(),t3.get_price())
if service=="Meal":
    print(t4.get_description(),t4.get_price())

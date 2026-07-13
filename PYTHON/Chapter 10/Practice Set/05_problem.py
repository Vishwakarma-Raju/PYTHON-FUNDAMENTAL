from random import randint

class Train():

    def __init__(self , trainNo):
        self.trainNo = trainNo

    def book(self , fromm, to):
        print(f"Ticket is booked in train no.{self.trainNo} from {fromm} to {to}")

    def getStatus(self):
        print(f"The Train No.{self.trainNo} is running on time.")

    def getFair(self, fromm, to):
        print(f"Ticket fare in train no.{self.trainNo} from {fromm} to {to} is {randint(299,999)}")

t = Train(12996)
t.book("Ahmedabad","Surat")
t.getStatus()
t.getFair("Ahmedabad","Surat")

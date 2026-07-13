from random import randint

class Train():

    def __init__(raju , trainNo):
        raju.trainNo = trainNo

    def book(raju , fromm, to):
        print(f"Ticket is booked in train no.{raju.trainNo} from {fromm} to {to}")

    def getStatus(raju):
        print(f"The Train No.{raju.trainNo} is running on time.")

    def getFair(raju, fromm, to):
        print(f"Ticket fare in train no.{raju.trainNo} from {fromm} to {to} is {randint(299,999)}")

t = Train(12996)
t.book("Ahmedabad","Surat")
t.getStatus()
t.getFair("Ahmedabad","Surat")

#There is no error after changing the argument : self to raju
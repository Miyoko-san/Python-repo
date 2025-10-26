# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.


from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro , to):
        print(f"Train ticket is booked for {self.trainNo} from {fro} to {to}")

    def getStatus(self, fro , to):
        print(f"Train no: {self.trainNo} is running on time.")
    
    def getFare(self, fro , to):
        print(f"Ticket fare in {self.trainNo} from {fro} to {to} is : {randint(200,5000)}")

t = Train(1234)
t.book("Delhi","Agra")
t.getStatus("Delhi","Agra")
t.getFare("Delhi","Agra")
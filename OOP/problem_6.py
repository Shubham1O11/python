import random
class train:
    def __init__(slf,trainNo):
        slf.trainNo=trainNo

    def book(self,fro,to):
        print(f"The ticket is book in train no:{self.trainNo} from {fro} to {to}")

    def getStatus(self,fro,to):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self,fro,to):
        print(f"ticket fare in train no: {self.trainNo} from {fro} to {to} is {random.randint(222,5555)}")

t=train(12939)
t.book("Nasik","Mumbai")
t.getStatus("Nasik","Mumbai")
t.getFare("Nasik","Mumbai")
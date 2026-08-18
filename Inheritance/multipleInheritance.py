class employee:
    company = "ITC"
    name="Default name"
    def show(self):
        print(f"The name of employee is {self.name} and The salary is {self.language}")

class coder:
    language = "python"
    def printlanguage(self):
        print(f"Out of all the languages here is your language: {self.language}")
class programmer (employee,coder):
    company="ICT infotech"
    def showlanguage (self):
        print(f"The name is {self.name} and He is good with {self.language} language")

a=employee()
p=programmer()

p.show()
p.printlanguage()
p.showlanguage()
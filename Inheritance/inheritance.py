class employee:
    company = "ITC"
    def show(self):
        print(f"The name of employee is {self.salary} and The salary is {self.salary}")

class programmer (employee):
    company="ICT infotech"
    def showlanguage (self):
        print(f"The name is {self.name} and He is good with {self.language} language")

a=employee()
p=programmer()

print(a.company, p.company)
class employee:
    language="python"
    salary=1200000

    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet(): 
        print("Good Morning")


shubham=employee("Shubham",1300000,"CPP")
# shubham.name="Shubham"
print(shubham.language,shubham.salary,shubham.name)

  
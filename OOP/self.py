class employee:
    language="python"
    salary=1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


shubham=employee()
shubham.name="Shubham"
# print(shubham.language,shubham.salary)

shubham.getInfo()
shubham.greet()
# employee.getInfo(shubham)
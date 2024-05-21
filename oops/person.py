class Person:
    def __init__(self,name, age, address):
        self.name =name
        self.age =age
        self.address =address
    def __str__(self):
        return f"Name: {self.name}, AGE:{self.age},Address:{self.address}"
p1 = Person("kartik",25,"hdfkshkahskfsgdh")
p2 = Person("Nikita",25,"jsdhfkjhsdfha")

print(p1)
print(p2)
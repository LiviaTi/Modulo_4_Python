class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def birthday(self)->None:
        self.age += 1
        return

p = Person("Livia", 24)
print(p.name,p.age)
p.birthday()
print(p.name,p.age)
import sys

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def birthday(self)->None:
        self.age += 1
        return

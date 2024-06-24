'''
for any class, a client should be able to use any of its subtypes indistinguishably, without even noticing, 
and therefore without compromising the expected behavior at runtime. This means that clients are completely 
isolated and unaware of changes in the class hierarchy.
In simpler terms means that a subclass, child or specialization of an object or class must be suitable by its Parent or SuperClass.
Subtypes must be substitutable for their base types
Use inheritance only when superclass is replacable by subclass in all the instances

Increases code reusability: By following LSP, we can create a set of related classes that can be used interchangeably without 
modifying the code. This makes it easier to reuse code and can save us time when we're developing new features.
'''

class SuperClass:
	def check(name: str)-> str:
		return name

class SubClass(SuperClass):
	def check(name: dict) -> dict:
		return name

class AnotherSubclass(SuperClass):
		def check(name: str, surname: str) -> tuple:
			return name, surname
                
from abc import ABC, abstractmethod

class Member(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def save_database(self):
        pass

class Teacher(Member):
    def __init__(self, name: str, age: int, teacher_id: str):
        super().__init__(name, age)
        self.teacher_id = teacher_id

    def save_database(self):
        print("Saving teacher data to database")

class Student(Member):
    def __init__(self, name: str, age: int , student_id: str):
        super().__init__(name, age)
        self.student_id = student_id

    def save_database(self):
        print("Saving student data to database")

from typing import List
members: List[Member] = []
members.apped(Student('nusret',23,"12345"))
members.apped(Teacher('Teacher_nusret',23,"12345"))
for member in members:
	member.save_database()
from Task1 import Person
from Task2 import Game
from Task3 import decorator_1

import ast
import random
import json

if __name__ == '__main__':
    #Task 1
    print("Welcome! Let's get to know each other!")
    firstName = str(input("your first name: "))
    lastName = str(input("your last name: "))
    age = int(input("your age: "))
    major = str(input("your major: "))
    hobby = str(input("your hobby: "))

    person = Person(firstName = firstName, lastName = lastName, age = age, major = major, hobby = hobby)


    #Task 2
    print("Let's play game!")
    n = int(input("How many times do you want to play: "))

    array = []
    while n:
        item = input("Enter data: ")

        try:
            item = json.loads(item)
        except:
            pass

        array.append(item)
        n -= 1

    game = Game(array)
    converted = game.typeBasedTransformer()

    for old, new in converted.items():
        print(f"Old value: {old}; New value: {new}")

    #Task 3

    @decorator_1
    def func():
        print("I am ready to Start")
        result = 0
        n = random.randint(10, 751)
        for i in range(n):
            result += (i ** 2)


    @decorator_1
    def funx(n=2, m=5):
        print("I am ready to do serious stuff")
        max_val = float('-inf')
        n = random.randint(10, 751)
        res = [pow(i, 2) for i in range(n)]
        for i in res:
            if i > max_val:
                max_val = i


    func()
    funx()
    func()
    funx()
    func()



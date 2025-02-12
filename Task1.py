class Person:
    def __init__(self, **Vals):
        self.__dict__.update(Vals)
        self.kwargsAcceptFun()

    def kwargsAcceptFun(self):
        print(f"Hello {self.__dict__.get('firstName', 'someone')} {self.__dict__.get('lastName', 'someone')}! "
              f"You are {self.__dict__.get('age', 0)} years old, studying {self.__dict__.get('major', 'nothing')}, "
              f"and enjoy {self.__dict__.get('hobby', 'nothing')}. Nice to meet you!")


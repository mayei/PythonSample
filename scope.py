class Person:
    def __init__(self,name,age,mark):
        self.name = name
        self.age = age
        self.mark = mark


    def say_name(self):
        print('Hello, my name is ', self.name)

    def say_age(self):
        print('I am',self.age, 'years old.')
        print('I got', self.mark)

p = Person('U Ba','50','95')
p.say_name() #Person.say_name()
p.say_age() # Person.say_age()
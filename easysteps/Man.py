from Person import *

"""A derived class"""

class Man(Person):
    
    def speak(self, msg):
            print(self.name, ':\n\tHello!',msg) 
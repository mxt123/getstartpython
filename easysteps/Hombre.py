from Person import *

"""A derived class"""

class Hombre(Person):
    
    def speak(self, msg):
            print(self.name, ':\n\tHola!',msg) 
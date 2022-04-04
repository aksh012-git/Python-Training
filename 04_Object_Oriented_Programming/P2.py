# Create classes according to the following class map:
# ->  Animal => Wild => Leopard, Tiger
# 	=> Pet => Dog
# 	=> Canine => Fox
# -> Each class contains two methods to get a name and info. Get the name returns the name of that animal and get the info returns hierarchy.
# For example,
# print(dog.get_name())  ⇒ My name is Tommy
# print(dog.get_info())  ⇒  I am Dog. I am Pet. I am Animal

class Animal():
    def __init__(self,name):
        self.name = name
        
    def get_name(self):
        return 'My name is ' + self.name
        
    def get_info(self):
        return "I am Animal"


class Wild(Animal):
    def get_name(self):
        return 'My name is ' + self.name
        
    def get_info(self):
        return "I am Wild. " + super().get_info()
 

class Pet(Animal):
   def get_name(self):
        return 'My name is ' + self.name
        
   def get_info(self):
        return "I am Pet. " + Animal.get_info(self)



class Canine(Animal):
    def get_name(self):
            return 'My name is ' + self.name
        
    def get_info(self):
        return "I am Canine. " + Animal.get_info(self)


class Leopard(Wild):
    def get_name(self):
            return 'My name is ' + self.name
        
    def get_info(self):
        return "I am Leopard. " + Wild.get_info(self)


class Tiger(Wild):
    def get_name(self):
            return 'My name is ' + self.name
        
    def get_info(self):
        return "I am Tiger. " + super().get_info()


class Dog(Pet):
    def get_name(self):
            return 'My name is ' + self.name
        
    def get_info(self):
        return "I am Dog. " + Pet.get_info(self)


class Fox(Canine):
    def get_name(self):
            return 'My name is ' + self.name
        
    def get_info(self):
        return "I am Fox. " + Canine.get_info(self)

dog = Tiger('tommy')
print(dog.get_name())
print(dog.get_info())
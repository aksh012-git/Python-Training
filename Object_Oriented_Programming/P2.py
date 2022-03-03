# Create classes according to the following class map:
# ->  Animal => Wild => Leopard, Tiger
# 	=> Pet => Dog
# 	=> Canine => Fox
# -> Each class contains two methods to get a name and info. Get the name returns the name of that animal and get the info returns hierarchy.
# For example,
# print(dog.get_name())  ⇒ My name is Tommy
# print(dog.get_info())  ⇒  I am Dog. I am Pet. I am Animal

class Animal():
    def __init__(self):
        


class Wild(Animal):
 



class Pet(Animal):
    pet = 'I am pild'



class Canine(Animal):
    canine = 'I am canine'



class Leopard(Wild):
    def __init__(self,):



class Tiger(Wild):
    pass


class Dog(Pet):
    pass


class Fox(Canine):
    pass

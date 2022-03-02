# Create classes according to the following class map:
# ->  Animal => Wild => Leopard, Tiger
# 	=> Pet => Dog
# 	=> Canine => Fox
# -> Each class contains two methods to get a name and info. Get the name returns the name of that animal and get the info returns hierarchy.
# For example,
# print(dog.get_name())  ⇒ My name is Tommy
# print(dog.get_info())  ⇒  I am Dog. I am Pet. I am Animal

class Animal():
    pass

class Wild(Animal):
    
    pass

class Pet(Animal):
    pass

class Canine(Animal):
    pass
    
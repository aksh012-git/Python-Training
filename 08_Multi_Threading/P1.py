from concurrent.futures import thread
from threading import *
import time

variable = 1
        
def sum():
    for i in range(20):
        global variable
        variable += 1
        print(variable)
        
def mult():
    for i in range(20):
        global variable
        variable -= 1
        print(variable)

thread_1 = Thread(target=sum)
thread_2 = Thread(target=mult)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()        
            
    

            


# Share single variable between two continuous loops.

from concurrent.futures import thread
from threading import *
import time

variable = 1
        
def sum(lock):
    for i in range(20):
        lock.acquire()
        global variable
        variable += 1
        lock.release()
        print(variable,'thread_1')
        
def sub(lock):
    for i in range(20):
        lock.acquire()
        global variable
        variable -= 1
        lock.release()
        print(variable, 'thread_2')

lock = Lock()
thread_1 = Thread(target=sum,args=(lock,))
thread_2 = Thread(target=sub,args=(lock,))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()        
            
    

            


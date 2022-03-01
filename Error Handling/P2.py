# 2. Create while loop which increase counter by one every second.
# -> Start count from 0
# -> Stop while loop when counter is grater than 500
# -> Program must not stop on any keyboard press. (Not even ctrl + c or ctrl + x) (edited) 

# go to vartual Envirment and write command
# sudo idle
# exec(open('/home/wot-aksh/Desktop/Python_Training/Error Handling/P2.py').read())

import time

x=0
while x <= 500:
    try:
        print (x)
        time.sleep(1)
        x=x+1
    except KeyboardInterrupt:
        pass

    
    
    

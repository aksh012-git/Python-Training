import threading

import time
# global variable x
x = 0


def thread_task(name):
    for i in range(10):
        global x
        x += 1
        print("For Thread :", name, x)
        # time.sleep(1)

def main_task():
    global x
    # setting global variable x as 0

    # creating threads
    t1 = threading.Thread(target=thread_task, args=(1, ))
    t2 = threading.Thread(target=thread_task, args=(2, ))

    # start threads
    t1.start()
    t2.start()

    # wait until threads finish their job
    t1.join()
    t2.join()


if __name__ == "__main__":
	# for i in range(10):
	main_task()
		# print("Iteration {0}: x = {1}".format(i,x))

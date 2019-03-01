'''This problem was asked by Apple.

Implement a job scheduler
 which takes in a function f and an integer n, 
 and calls f after n milliseconds.
'''

'''
#this is the beginner approach
import time
startTime = time.time() # time we start the program
def f(n):
    global startTime
    endtime = time.time() - startTime
    if endtime >= n:
        print("1 cycle ended")
        startTime = time.time()

        return True
while True:
    f(1)
'''
#more advanced way
import threading

def jobToDo():
    print("Job's done")

def f(n):
    threading.Timer(n,f, [n]).start()
    jobToDo()


f(10)
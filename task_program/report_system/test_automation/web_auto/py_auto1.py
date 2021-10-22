import functools
import time

import schedule


# This decorator can be applied to
def with_logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('LOG: Running job "%s"' % func.__name__)
        result = func(*args, **kwargs)
        print('LOG: Job "%s" completed' % func.__name__)
        return result

    return wrapper

@with_logging
def job():
    print('Hello, World.')

def writing():
    with open('helloworld.txt','a') as f:
        f.write("hello world ")
        f.close()

schedule.every(3).seconds.do(writing)

while 1:
    schedule.run_pending()
    time.sleep(1)




# import schedule
# import time
# import os 
# import psutil
# import multiprocessing

# # def callme():
# #     print("hello world")



# schedule.every(2).seconds.do(writing)

# writing()



# def job():
#     print("I'm working...")

# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)



# def getTasks(name):
  
#     for i in range(len(r)):
#         s = r[i]
#         if name in r[i]:
#             print ('%s in r[i]' %(name))
#             return r[i]
#     return []


# r = getTasks(imgName)



# print(r)

# r = os.popen('tasklist /v').read().strip().split('\n')
# print(r)

# print ('# of tasks is %s' % (len(r)))
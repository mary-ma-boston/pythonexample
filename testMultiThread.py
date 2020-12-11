import logging
import threading
import time
from multiprocessing import Lock, Process, Queue, current_process
import time
import queue
import requests

globalNum = 5
# print("ttttttttttttttt", globalNum)
# print(__name__)

def thread_function(name): ###########
    global globalNum
    logging.info("Thread %s: starting", name)
    time.sleep(10)
    globalNum += 1
    logging.info("Thread %s: finishing global num is %s", name, str(globalNum))


def testMultiThread():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    x = threading.Thread(target=thread_function, args=(1,)) ###########
    x.start()  ############

    x2 = threading.Thread(target=thread_function, args=(2,)) ###########
    x2.start()  ############


def testMultiProcess():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    p = Process(target=testMultiThread)
    p.start()

    p2 = Process(target=testMultiThread)
    p2.start()

    p.join()
    p2.join()

def testRestAPI():
    resp = requests.get('http://dummy.restapiexample.com/api/v1/employees')
    if resp.status_code != 200:
        print("error")
    jsonData = resp.json()
    for onePersonInfo in jsonData["data"]:
        if onePersonInfo["employee_name"] == "Quinn Flynn" and onePersonInfo["employee_age"] == "23":
            print("Find stupid person")

        # print(onePersonInfo["employee_name"])

if __name__ == "__main__":
    # testMultiThread()
    # testMultiProcess()
    testRestAPI()


    
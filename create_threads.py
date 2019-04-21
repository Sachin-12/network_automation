import threading
import time
#Creating threads
def create_threads(function,list):

    threads = []
    i = 0
    for ip in list:
        th = threading.Thread(target=function,args=(ip,i,))   #args is a tuple with a single element
        th.start()
        threads.append(th)
        # time.sleep(5)
        i = i+1

    for th in threads:
        th.join()


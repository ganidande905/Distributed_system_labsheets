from multiprocessing import Process, Value , Lock
import time


def incrementer(shared_value, lock , name):
    print(f"Process {name} is starting....")
    
    with lock:
        temp = shared_value.value
        time.sleep(1)
        shared_value.value = temp + 1
        print(f"Process {name} incremented value")

def printer(shared_value):
    time.sleep(2)
    print(f"Process printer reading value: : {shared_value.value}")
    
if __name__ == "__main__":
    shared_value = Value('i', 0)
    lock = Lock()
    
    p1 = Process(target=incrementer, args=(shared_value, lock, 'Incrementer 1'))
    p2 = Process(target=incrementer, args=(shared_value, lock, 'Incrementer 2'))
    p3 = Process(target=printer, args=(shared_value,))
    
    p1.start()
    p2.start()
    p3.start()
    
    p1.join()
    p2.join()
    p3.join()
    
    print("Final shared value:", shared_value.value)
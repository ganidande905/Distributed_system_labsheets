from multiprocessing import Process, Value, Array, Lock

def modify_integer(shared_int, lock):
    with lock:
        shared_int.value = 1
        print("Process 1 modified integer to", shared_int.value)

def modify_float(shared_float, lock):
    with lock:
        shared_float.value = 3.14
        print("Process 2 modified float to", shared_float.value)

def modify_string(shared_string, lock):
    with lock:
        message = "Hello"
        shared_string.value = message.encode()  
        print("Process 3 modified string to", message)

if __name__ == "__main__":
    
    # Create shared memory objects
    shared_int = Value('i', 0)           
    shared_float = Value('d', 0.0)       
    shared_string = Array('c', 20)       
    
    lock = Lock()
    p1 = Process(target=modify_integer, args=(shared_int, lock))
    p2 = Process(target=modify_float, args=(shared_float, lock))
    p3 = Process(target=modify_string, args=(shared_string, lock))
    p1.start()
    p2.start()
    p3.start()

    # Wait for completion
    p1.join()
    p2.join()
    p3.join()
    final_string = shared_string.value.decode().strip('\x00')

    print("Final array:", [shared_int.value, shared_float.value, final_string])
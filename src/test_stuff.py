import threading
 
 
def first_func():
    for x in range(100):
        print('one: ',x)
 
 
def second_func():
    for x in range(100):
        print('two: ',x)
 
 
if __name__ =="__main__":
    t1 = threading.Thread(target=first_func)
    t2 = threading.Thread(target=second_func)
 
    t1.start()
    t2.start()
 
    t1.join()
    t2.join()
 
    print("Done!")
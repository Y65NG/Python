import threading
import time

class Thread(threading.Thread):
    def __init__(self, name, id):
        threading.Thread.__init__(self)
        self.name = name
        self.lock = threading.Lock()

    def run(self):
        print("Starting " + self.name)
        self.lock.acquire()
        self.func(1)
        self.lock.release()
        print("Exiting " + self.name)
        return 'lalala'
    
    def func(self, t):
        print('Thread:', self.name)
        time.sleep(t)
    
threads = []

t1 = Thread('t1', 1)
t2 = Thread('t2', 2)

a = t1.start()
print(t1.run())
t2.start()

threads.append(t1)
threads.append(t2)

for t in threads:
    t.join()
print('quit')

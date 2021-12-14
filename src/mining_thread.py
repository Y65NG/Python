import hashlib
import threading
import time
import queue

def find(word, diff, start, end, start_time):
    for i in range(start, end):
        binary = (word + str(i)).encode('utf-8')
        sha = hashlib.sha3_256(binary).hexdigest()
        if sha[:diff] == '0' * diff:
            print(sha)
            print(time.time() - start_time, 'seconds')
            # q.put(sha)
            print()
            return i - start
		

if __name__ == '__main__':
    index = 0
    n = 10000
    r = 1 * 10 ** 8
    word = 'An apple a day keeps the doctor away'
    threads = []
 
    start = time.time()
    for i in range(1, r, n):
        t = threading.Thread(target=find, args=(word, 6, i, i + n, start))
        t.start()
        
        threads.append(t)
        
	
    end = time.time()
    print('Whole program ends in:', end - start, 'seconds')
    for t in threads:
        t.join()
	# print(find('An apple a day keeps doctor away', 7))


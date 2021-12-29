import sys
 
def fibonacci(n): 
    a, b, counter = 0, 1, 0
    # while True:
    print('before')
    if (counter > n): 
        return
    yield a
    a, b = b, a + b
    counter += 1
    print('after')
f = fibonacci(10) 
print(f)

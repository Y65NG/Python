import sys
 
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    # while True:
    print('before')
    if (counter > n): 
        return
    yield a
    a, b = b, a + b
    counter += 1
    print('after')
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
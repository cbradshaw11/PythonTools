import time

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2)

start = time.time()
print("Running Fib!")
print(fib(40))
end = time.time()
print("Runtime in secs:")
print(end-start)

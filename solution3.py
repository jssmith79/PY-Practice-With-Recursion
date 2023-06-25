# Write code for algorithm 3 below

def fib(n):
    if n<= 0:
        print("invalid input")
    elif n ==1:
        return 0
    elif n == 2:
        return 1
    else: 
        return fib(n-1) + fib(n-2)
print("2nd fib number:")
print(fib(2))
print("4th fib number:")
print(fib(4))
print("8th fib number:")
print(fib(8))
# Write code for algorithm 4 below

def exp(a,b):
    if b < 1:
        print("invalid input")
    elif b == 1:
        return a
    else:
        return a * exp(a,b=1)

print ("3^1:")
print(exp(3,1))
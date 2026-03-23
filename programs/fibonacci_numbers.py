import sys
def fib_n():
    print("Fibonacci Numbers")
    print("------------------------------")
    print("Enter the value of n")
    n = int(input(""))
    print("------------------------------")
    print("Do you want output of the full sequence? Leave empty for no")
    ans = input("")
    onList = (ans != "")
    print("------------------------------")
    a, b = 1, 1
    if onList:
        sys.stdout.write(str(a) + ", ")
        sys.stdout.write(str(b) + ", ")
    for i in range(n - 2):
        
        a,b = b, a+b
        if onList:
            sys.stdout.write(str(b) + ", ")
    if onList:
        sys.stdout.write("\b\b ")
        print("")
        print("------------------------------")
    print(f"Result is: {b}")
    print("------------------------------")
    return a
    
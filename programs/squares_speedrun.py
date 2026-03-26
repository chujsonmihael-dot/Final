import time
def returnSquares(n, mode):
    oldTIme = time.time()
    
    if mode == "naive":
        NaiveSquares(n)
    elif mode == "shortmult":
        ShortMultSquares(n)
    elif mode == "diff":
        DiffSquares(n)
    else:
        print("Invalid mode")
    print("-------------------------------")
    return time.time() - oldTIme

def NaiveSquares(n):
    print("Naive Approach")
    for i in range(n+1):
        val = i*i
    print(val)
def ShortMultSquares(n):
    print("Short Mult Approach")
    val = 0
    for i in range(n):
        val += 2*i + 1
    print(val)
        
def DiffSquares(n):
    print("Diff Approach")
    val = 0
    diff = 1
    for i in range(n):
        
        val += diff
        diff += 2
    print(val)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print("-------------------------------")
    NaiveApproachTime = returnSquares(n, "naive")
    ShortMultApproachTime = returnSquares(n, "shortmult")
    DiffApproachTime = returnSquares(n, "diff")
    print("Naive Approach took: " + str(NaiveApproachTime))
    print("Short Mult Approach took: " + str(ShortMultApproachTime))
    print("Diff Approach took: " + str(DiffApproachTime))

import time
def n_queens(n):
    board = []
    result = []
    cols = set()
    diags1 = set()
    diags2 = set()
    backtrack(board, result,n, cols,diags1,diags2)
    return result
def backtrack(board, result, n, cols, diags1, diags2):
    row = len(board)
    if row == n:
        result.append(board.copy())
        return
    for col in range(n):
        if is_valid(row,col, cols, diags1, diags2):
            cols.add(col)
            diags1.add(row+col)
            diags2.add(row-col)
            board.append((row,col))
            backtrack(board, result, n, cols, diags1, diags2)
            board.pop()
            cols.remove(col)
            diags1.remove(row+col)
            diags2.remove(row-col)

def is_valid(r, c, cols, diags1, diags2):
    if c in cols or r+c in diags1 or r-c in diags2:
        return False
    return True


def main():
    print("N Queens")
    print("------------------------------")
    n = int(input("Enter value of n: "))
    startTime = time.time()

    ans = n_queens(n)
    endTime = time.time()
    print("------------------------------")
    print(f"Found {len(ans)} answers")
    print("------------------------------")
    print("All found Solutions:")
    for entry in ans:
        print(entry)
    print("------------------------------")
    print(f"Search took {endTime - startTime}")
    print("------------------------------")
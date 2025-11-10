def solve_n_queens(n):
    board, solutions = [0]*n, []
    def safe(r,c):
        return all(board[i] != c and abs(board[i]-c) != r-i for i in range(r))
    def backtrack(r):
        if r == n:
            solutions.append(board[:]); return
        for c in range(n):
            if safe(r,c):
                board[r] = c
                backtrack(r+1)
    backtrack(0)
    return solutions
def print_solutions(solutions):
    for sol in solutions:
        for r in range(len(sol)):
            print(" ".join("Q" if sol[r] == c else "." for c in range(len(sol))))
        print()
    print("Total Solutions:", len(solutions))
def main():
    try: n = int(input("Enter N: ") or 4)
    except: n = 4
    print_solutions(solve_n_queens(n))
if __name__ == "__main__":
    main()

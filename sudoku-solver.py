import copy
import time

tried_numbers = []
for a in range(9):
    tried_numbers.append([[], [], [], [], [], [], [], [], []])


def matrix(board):
    for r in range(9):
        print(board[r][0:3], "", board[r][3:6], "", board[r][6:9])
        if r == 2 or r == 5 or r == 8:
            print("")

#Code for checking if a number can go to that square or not
def posb(x, y, n):
    for i in grid[y]:
        if n == i:
            return False
    for u in range(9):
        if n == grid[u][x]:
            return False
    k = x // 3 * 3
    l = y // 3 * 3
    for z in range(3):
        for m in range(3):
            if n == grid[l + z][k + m]:
                return False
    return True

#Code that brute forces combinations and finds possible paths to the solution
def solve(retry):
    if retry:
        y = 8
        x = 8
    else:
        y = 0
        x = 0
    try:
        while y <= 8:
            while x <= 8:
                n = 1
                while n <= 9:
                    if identity[y][x] != 0:
                        if x != 8:
                            x += 1
                        else:
                            x = 0
                            y += 1
                        break
                    if identity[y][x] == 0 and posb(x, y, n) and n not in tried_numbers[y][x]:
                        grid[y][x] = n
                        tried_numbers[y][x].append(n)
                        n = 1
                        if x != 8:
                            x += 1
                        else:
                            y += 1
                            x = 0
                    elif identity[y][x] == 0 and n not in tried_numbers[y][x] and not posb(x, y, n):
                        tried_numbers[y][x].append(n)
                        n += 1
                    if n in tried_numbers[y][x]:
                        n += 1
                    if tried_numbers[y][x] == [1, 2, 3, 4, 5, 6, 7, 8, 9] and identity[y][x] == 0:
                        grid[y][x] = 0
                        tried_numbers[y][x] = []
                        if x != 0:
                            x -= 1
                            n = 1
                            while identity[y][x] != 0:
                                if x != 0:
                                    x -= 1
                                else:
                                    y -= 1
                                    x = 8
                            grid[y][x] = 0
                        else:
                            y -= 1
                            x = 8
                            while identity[y][x] != 0:
                                if x != 0:
                                    x -= 1
                                else:
                                    y -= 1
                                    x = 8
                            grid[y][x] = 0
    except:
        print("Done!")
        matrix(grid)
        if retry:
            return
        answer = input("Do you want to try and find other solutions?")
        if answer == "No":
            return
        if answer == "Yes":
            return solve(True)


grid = [
    [4, 0, 0,  0, 1, 0,  0, 0, 0],
    [0, 9, 0,  0, 0, 0,  2, 0, 0],
    [0, 0, 3,  5, 0, 4,  0, 6, 0],

    [3, 0, 0,  0, 0, 0,  0, 0, 4],
    [0, 0, 0,  0, 0, 8,  0, 0, 0],
    [0, 0, 4,  7, 0, 6,  0, 5, 0],

    [0, 0, 7,  0, 8, 0,  0, 0, 0],
    [2, 0, 0,  1, 0, 7,  6, 0, 0],
    [0, 0, 0,  0, 3, 0,  0, 1, 0]
]
identity = copy.deepcopy(grid)

matrix(grid)
solve(False)
print(time.process_time())
"""grid = [
    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0],

    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0],

    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0]
]"""

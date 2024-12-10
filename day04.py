# --- Day 4: Ceres Search ---

def day04_a(input):
    matrix = []
    with open(input) as file:
        for line in file:
            matrix.append(list(line.strip()))
    
    height = len(matrix)
    width = len(matrix[0])

    total_xmas_found = 0
    xmas = ['X', 'M', 'A', 'S']

    for row in range(height):
        for col in range(width):
            # check if each character is X until hit, then check directions for word
            if matrix[row][col] == 'X':
                # check left
                if col >= 3:
                    valid = True
                    for i in range(1, 4):
                        if matrix[row][col - i] != xmas[i]:
                            valid = False
                            break
                    if valid:
                        total_xmas_found += 1
                # check up left
                if col >= 3 and row >= 3:
                    valid = True
                    for i in range(1, 4):
                        if matrix[row - i][col - i] != xmas[i]:
                            valid = False
                            break
                    if valid:
                        total_xmas_found += 1
                # check up
                if row >= 3:
                    valid = True
                    for i in range(1, 4):
                        if matrix[row - i][col] != xmas[i]:
                            valid = False
                            break
                    if valid:
                        total_xmas_found += 1
                # check up right
                if row >= 3 and col <= width - 4:
                    valid = True
                    for i in range(1, 4):
                        if matrix[row - i][col + i] != xmas[i]:
                            valid = False
                            break
                    if valid:
                        total_xmas_found += 1
                # check right
                if col <= width - 4:
                    valid = True
                    for i in range(1, 4):
                        if matrix[row][col + i] != xmas[i]:
                            valid = False
                            break
                    if valid:
                        total_xmas_found += 1
                # check down right
                if row <= height - 4 and col <= width - 4:
                    valid = True
                    for i in range(1, 4):
                        if matrix[row + i][col + i] != xmas[i]:
                            valid = False
                            break
                    if valid:
                        total_xmas_found += 1
                # check down
                if row <= height - 4:
                    valid = True
                    for i in range(1, 4):
                        if matrix[row + i][col] != xmas[i]:
                            valid = False
                            break
                    if valid:
                        total_xmas_found += 1
                # check down left
                if row <= height - 4 and col >= 3:
                    valid = True
                    for i in range(1, 4):
                        if matrix[row + i][col - i] != xmas[i]:
                            valid = False
                            break
                    if valid:
                        total_xmas_found += 1
    
    print (total_xmas_found)

day04_a('day04_input.txt')

def day04_b(input):
    matrix = []
    with open(input) as file:
        for line in file:
            matrix.append(list(line.strip()))

    height = len(matrix)
    width = len(matrix[0])

    total_xmas_found = 0

    for row in range(height):
        for col in range(width):
            # check if each character is A until hit, then check diagonals for MAS
            if matrix[row][col] == 'A' and col >= 1 and col <= width - 2 and row >= 1 and row <= height - 2:
                if ((matrix[row - 1][col - 1] == 'M' and matrix[row + 1][col + 1] == 'S') or (matrix[row - 1][col - 1] == 'S' and matrix[row + 1][col + 1] == 'M')) and ((matrix[row - 1][col + 1] == 'M' and matrix[row + 1][col - 1] == 'S') or (matrix[row - 1][col + 1] == 'S' and matrix[row + 1][col - 1] == 'M')):
                    total_xmas_found += 1
    print (total_xmas_found)

day04_b('day04_input.txt')

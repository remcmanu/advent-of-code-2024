# --- Day 1: Historian Hysteria ---

# import os

def day01_a(input):
    file = open(input, "r")

    left = []
    right = []

    for line in file:
        line = line.split('   ')
        left.append(int(line[0]))
        right.append(int(line[1].split('\n')[0]))
    
    file.close()
    
    left.sort()
    right.sort()

    distance = 0

    for i in range (len(left)):
        distance += abs(left[i] - right[i])

    print(distance)


day01_a("day01_input.txt")
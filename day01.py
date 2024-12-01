# --- Day 1: Historian Hysteria ---

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

def day01_b(input):
    file = open(input, "r")

    left = []
    right = []

    for line in file:
        line = line.split('   ')
        left.append(int(line[0]))
        right.append(int(line[1].split('\n')[0]))
    
    file.close()

    similarity = 0
    count = 0
    for left_item in left:
        for right_item in right:
            if left_item == right_item:
                count += 1
        similarity += left_item * count
        count = 0
    print(similarity)

day01_b("day01_input.txt")
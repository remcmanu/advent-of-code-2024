# --- Day 2: Red-Nosed Reports ---

def day02_a(input):
    file = open(input, "r")

    solid_reports = 0
    for line in file:
        numbers = line.strip().split(' ')
        increasing = None
        prev = None
        valid = True
        for number in numbers:
            number = int(number)
            # second or more iterations
            if prev != None:
                distance = number - prev
                
                # check if changed by at least one, at most than 3
                if abs(distance) < 1 or abs(distance) > 3:
                    prev = number
                    valid = False
                    continue
                
                # check if increasing / decreasing first time
                if increasing == None:
                    increasing = True if distance > 0 else False
                
                # check if increasing / decreasing other times
                if (distance < 0 and increasing) or (distance > 0 and not increasing):
                    prev = number
                    valid = False
                    continue

            
            prev = number
        if valid:
            solid_reports += 1
    
    file.close()
    print(solid_reports)

day02_a("day02_input.txt")


def day02_b(input):
    file = open(input, "r")

    solid_reports = 0
    for line in file:
        numbers = line.strip().split(' ')
        valid = check_valid(numbers)
        if valid:
            solid_reports += 1
        
        else:
            for i in range(len(numbers)):
                temp_numbers = list(numbers)
                temp_numbers.pop(i)
                valid = check_valid(temp_numbers)
                if valid:
                    solid_reports += 1
                    break
    print (solid_reports)

def check_valid(numbers):
    increasing = None
    prev = None
    valid = True
    for number in numbers:
        number = int(number)
        # second or more iterations
        if prev != None:
            distance = number - prev
            
            # check if changed by at least one, at most than 3
            if abs(distance) < 1 or abs(distance) > 3:
                prev = number
                valid = False
                continue
            
            # check if increasing / decreasing first time
            if increasing == None:
                increasing = True if distance > 0 else False
            
            # check if increasing / decreasing other times
            if (distance < 0 and increasing) or (distance > 0 and not increasing):
                prev = number
                valid = False
                continue

        
        prev = number
    return valid

day02_b("day02_input.txt")
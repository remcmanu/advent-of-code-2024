# --- Day 3: Mull It Over ---

def day03_a (input):
    file = open(input, "r")


    result = 0
    for line in file:
        start = None # start of a potential mul sequence
        current = 0 # character being analyzed currently
        multiplier = None
        multiplicand = None

        for i in range(len(line)):
            
            char = line[i]
            print ("[ " + str(i) + " ]" + " CHAR IS: " + char)
            
            # skip if char not m and not in sequence
            if start == None and char != 'm':
                print (char + " SKIP")
                continue
            # starting new sequence
            if start == None and char == 'm':
                start = i
                current = i + 1
                print (char + " m")
                continue
            # currently in a sequence
            if start != None:
                match char:
                    # is u
                    case 'u':
                        if line[current - 1] != 'm':
                            start = current = multiplier = multiplicand = None
                            print (char + " u")
                            continue
                    # is l
                    case 'l':
                        if line[current - 1] != 'u':
                            start = current = multiplier = multiplicand = None
                            print (char + " l")
                            continue
                    # is (
                    case '(':
                        if line[current - 1] != 'l':
                            start = current = multiplier = multiplicand = None
                            print (char + " (")
                            continue
                    # is number
                    case str(char) if char.isdigit():
                        print ("IS INT")
                        # is first digit of multiplier
                        if line[current - 1] == '(':
                            multiplier = int(char)
                        # is first digit of multiplicand
                        elif line[current - 1] == ',':
                            multiplicand = int(char)
                        # is another digit of multiplicand
                        elif multiplicand != None:
                            multiplicand = multiplicand * 10 + int(char)
                        # is another digit of multiplier
                        elif multiplicand == None and multiplier != None:
                            multiplier = multiplier * 10 + int(char)
                        else:
                            start = current = multiplier = multiplicand = None
                            continue
                    # is ,
                    case ',':
                        print (char + " ,")
                        # if not after number
                        if not line[current - 1].isnumeric():
                            start = current = multiplier = multiplicand = None
                            continue
                        # if multiplicand was number preceding
                        elif multiplicand != None:
                            start = current = multiplier = multiplicand = None
                            continue
                    # is )
                    case ')':
                        print (char + ' )')
                        # if not after number
                        if not line[current - 1].isnumeric():
                            start = current = multiplier = multiplicand = None
                            continue
                        # if multiplicand was not number preceding
                        elif multiplicand == None:
                            start = current = multiplier = multiplicand = None
                            continue
                        else: 
                            print ("multiplying " + str(multiplier) + ' ' + str(multiplicand))
                            print ("MUL EXPRESSION: " + line[start:current])
                            result += multiplier * multiplicand
                            start = current = multiplier = multiplicand = None
                            continue
            # move pointer
            current += 1
    print (result)

# day03_a('day03_input_small.txt')
day03_a('day03_input.txt')
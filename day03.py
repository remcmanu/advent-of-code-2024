# --- Day 3: Mull It Over ---

def day03_a (input):
    with open(input, "r") as file:

        result = 0

        for line in file:
            start = None        # index of the m character in a potential mul(X,Y) sequence
            multiplier = None   # left hand # of mul
            multiplicand = None # right hand # of mul

            for i, char in enumerate(line):
                # start a sequence when not in one and m character appears
                if start == None and char == 'm':
                    start = i
                elif start != None:
                    # if character is 'u' and expression is currently 'm'
                    if char == 'u' and line[start:i] == 'm':
                        continue
                    # if character is 'l' and expression is currently 'mu'
                    if char == 'l' and line[start:i] == 'mu':
                        continue
                    # if character is '(' and expression is currently 'mul'
                    if char == '(' and line[start:i] == 'mul':
                        multiplier = multiplicand = ""
                        continue
                    # if character is a digit and expression is currently 'mul(', start a new multiplier
                    if char.isdigit() and line[start:i] == 'mul(' + multiplier:
                        multiplier += char
                        continue
                    # if character is a ','
                    if char == ',': 
                        #  and expression matches as it should
                        if multiplier != None and line[start:i] == 'mul(' + multiplier:
                            continue
                        # if you have ',' before multiplier is set, it'll throw error
                        # TypeError: can only concatenate str (not "NoneType") to str
                        else:
                            print("FAILED: [" + char + "] " + line[start:i + 1])
                            start = multiplier = multiplicand = None
                    # if character is a digit and expression matches as it should, starta new multiplicand
                    if char.isdigit() and line[start:i] == 'mul(' + multiplier + ',' + multiplicand:
                        multiplicand += char
                        continue
                    # if character is a ')'
                    if char == ')':
                        # and expression matches as it should, do the math and reset
                        if multiplier != None and multiplicand != None and line[start:i] == 'mul(' + multiplier + ',' + multiplicand:
                            result += int(multiplier) * int(multiplicand)
                            print("MULTIPLIED: " + line[start:i + 1])
                            start = multiplier = multiplicand = None
                            continue
                        # if you have a ')' before either number is set, it'll throw error
                        # TypeError: can only concatenate str (not "NoneType") to str
                        else:
                            print("FAILED: [" + char + "] " + line[start:i + 1])
                            start = multiplier = multiplicand = None
                    else:
                        print("FAILED: [" + char + "] " + line[start:i + 1])
                        start = multiplier = multiplicand = None
        print (result)

# day03_a('day03_input_small.txt')
# day03_a('day03_input.txt')

def day03_b (input):
    with open(input, "r") as file:

        result = 0

        data = ""
        for line in file:
            data += line

        print (data)

        start = None        # index of the m character in a potential mul(X,Y) sequence
        multiplier = None   # left hand # of mul
        multiplicand = None # right hand # of mul
        enabled = True           # starts with mul instructions enabled (given)

        for i, char in enumerate(data):
            last_ten = data[i - 10: i + 1]
            # whether in mul sequence or not, if you see a ) character check for dos and such.
            if char == ')':
                if enabled and data[i - 6 : i + 1] == "don't()":
                    enabled = False
                    print ("DISABLED i: " + str(i))
                if not enabled and data[i - 3 : i + 1] == 'do()':
                    enabled = True
                    print ("ENABLED i: " + str(i))
            # start a sequence when mul structions enabled and when not in one and m character appears
            if enabled and start == None and char == 'm':
                start = i
            elif enabled and start != None:
                # if character is 'u' and expression is currently 'm'
                if char == 'u' and data[start:i] == 'm':
                    continue
                # if character is 'l' and expression is currently 'mu'
                if char == 'l' and data[start:i] == 'mu':
                    continue
                # if character is '(' and expression is currently 'mul'
                if char == '(' and data[start:i] == 'mul':
                    multiplier = multiplicand = ""
                    continue
                # if character is a digit and expression is currently 'mul(', start a new multiplier
                if char.isdigit() and data[start:i] == 'mul(' + multiplier:
                    multiplier += char
                    continue
                # if character is a ','
                if char == ',': 
                    #  and expression matches as it should
                    if multiplier != None and data[start:i] == 'mul(' + multiplier:
                        continue
                    # if you have ',' before multiplier is set, it'll throw error
                    # TypeError: can only concatenate str (not "NoneType") to str
                    else:
                        print("FAILED: [" + char + "] " + data[start:i + 1])
                        start = multiplier = multiplicand = None
                # if character is a digit and expression matches as it should, starta new multiplicand
                if char.isdigit() and data[start:i] == 'mul(' + multiplier + ',' + multiplicand:
                    multiplicand += char
                    continue
                # if character is a ')'
                if char == ')':
                    # and expression matches as it should, do the math and reset
                    if multiplier != None and multiplicand != None and data[start:i] == 'mul(' + multiplier + ',' + multiplicand:
                        result += int(multiplier) * int(multiplicand)
                        print("MULTIPLIED: " + data[start:i + 1])
                        start = multiplier = multiplicand = None
                        continue
                    # if you have a ')' before either number is set, it'll throw error
                    # TypeError: can only concatenate str (not "NoneType") to str
                    else:
                        print("FAILED: [" + char + "] " + data[start:i + 1])
                        start = multiplier = multiplicand = None
                else:
                    print("FAILED: [" + char + "] " + data[start:i + 1])
                    start = multiplier = multiplicand = None
        print (result)

# day03_b('day03_input_small.txt')
day03_b('day03_input.txt')


# NOTE:
# lmao, so i thought i needed to combine the lines of the input cause i might be missing a do, don't, or muls
# even though it didnt seem so looking at the 6 lines
# BUT it turns out i was resetting the enabled boolean after each line the way i was doing it
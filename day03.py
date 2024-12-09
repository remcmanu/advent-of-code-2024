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
day03_a('day03_input.txt')
def isDigit(input):
    if input.isdigit():
        return int(input)
    return 0

def iterate(input):
    # TODO: how to optimize that?
    for c in input:
        check = isDigit(c)
        if check == 0:
            continue
        return check
    return 0

def check_line(input):
    return int(str(iterate(input)) + str(iterate(input[::-1])))


def day11():
    f = open("input.txt", "r")
    count = 0
    for line in f:
        count = count + check_line(line)
    print(count)
    
    
if __name__ == '__main__':
    day11()
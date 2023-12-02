def isDigit(str):
    if str.isdigit():
        return int(str)
    return 0

def iterate(str):
    # TODO: how to optimize that?
    for c in str:
        check = isDigit(c)
        if check == 0:
            continue
        return check
    return 0

def check_line(str):
    return iterate(str) + iterate(str[::-1])


def day11():
    f = open("input.txt", "r")
    count = 0
    for line in f:
        count = count + check_line(line)
    print(count)
    
    
if __name__ == '__main__':
    day11()
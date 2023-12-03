numbers = dict (
    eight= "8",
    nine= "9",
    seven= "7",
    six= "6",
    five= "5",
    four= "4",
    three= "3",
    two= "2",
    one = "1",
)

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


def prepare(s):
    for k in range(len(numbers)):
        s = s.replace(list(numbers.keys())[k], list(numbers.values())[k])
    return s

def day11():
    f = open("./input.txt", "r")
    count = 0
    for line in f:
        count = count + check_line(line)
    print(count)


def day12():
    f = open("./input.txt", "r")
    count = 0
    for line in f:
        count = count + check_line(prepare(line))
    print(count)
    
if __name__ == '__main__':
    day11()
    day12()
import copy
# int code
innitCode = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0]


def part1(coode):
    code = copy.deepcopy(coode)
    for i in range(0, len(code), 4):
        op = code[i]
        if op == 1:
            code[code[i + 3]] = code[code[i + 1]] + code[code[i + 2]]
        elif op == 2:
            code[code[i + 3]] = code[code[i + 1]] * code[code[i + 2]]
        elif op == 99:
            return code[0]

def part2():
    for noun in range(0,99):
        for verb in range(0,99):
            coode = copy.deepcopy(innitCode)
            coode[1] = noun
            coode[2] = verb
            if part1(coode) == 19690720:
                return 100 * noun + verb



if __name__ == '__main__':
    print(part1(innitCode))
    print(part2())

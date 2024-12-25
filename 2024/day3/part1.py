import re
from functools import reduce

def splitLine(line: str) -> list[tuple[int, int]]:
    commands: list = re.findall("mul\(\d+,\d+\)", line)
    tups:list = list(map(lambda x: x[4:-1], commands))
    l = list(map(lambda x: tuple(x.split(',')), tups))
    return list(map(lambda x: ((int(x[0]), int(x[1]))), l))

def mulAdd(line: list[tuple[int, int]]) -> int:
    li = list(map(lambda x: x[0]*x[1], line))
    return reduce(lambda x,y: x+y, li)

if __name__ == "__main__":
    with open('inputs/input.txt', 'r') as f:
        line = f.readline()
        s = 0
        while line:
            s += mulAdd(splitLine(line))
            line = f.readline()

    print(f'Sum: {s}')


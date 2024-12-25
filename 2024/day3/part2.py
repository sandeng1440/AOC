import re
from functools import reduce

def splitLine(line: str, s: bool | None) -> tuple[list[tuple[int, int]] | None, bool]:
    commands: list = re.findall(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)", line)
    skip: bool = False if s == None else s
    remove: list[int] = []

    for i in range(len(commands)):
        if i == 0 and not skip:
            if "'" in commands[i]:
                skip = True
                remove.append(i)
                continue
            elif "d" in commands[i]:
                skip = False
                remove.append(i)
                continue
            

        if "'" in commands[i]:
            skip = True
            remove.append(i)
            continue

        if "d" in commands[i]:
            skip = False
            remove.append(i)

        if skip:
            remove.append(i)
            continue
    
    comms = [x for i,x in enumerate(commands) if i not in remove]

    tups:list = list(map(lambda x: x[4:-1], comms))
    l = list(map(lambda x: tuple(x.split(',')), tups))
    return list(map(lambda x: ((int(x[0]), int(x[1]))), l)), skip

def mulAdd(line: list[tuple[int, int]]) -> int:
    li = list(map(lambda x: x[0]*x[1], line))
    return reduce(lambda x,y: x+y, li)

if __name__ == "__main__":
    with open('inputs/input.txt', 'r') as f:
        line = f.readline()
        s = 0
        skip: bool | None = None
        while line:
            l, skip = splitLine(line, skip)
            s += mulAdd(l) if l else 0
            line = f.readline()

    print(f'Sum: {s}')


with open('inputs/input.txt', 'r') as file:
    line: str = file.readline().rstrip('\n')
    list1: list[int] = []
    list2: list[int] = []

    while line:
        l: list[str] = line.split(' ')
        list1.append(int(l[0]))
        list2.append(int(l[-1]))
        line = file.readline().rstrip('\n')
    
    list1.sort()
    list2.sort()

    tups = list(zip(list1, list2))
    dist = 0
    for tup in tups:
        dist += abs(tup[0] - tup[1])

    print(f'\nTotal Distance: {dist}')


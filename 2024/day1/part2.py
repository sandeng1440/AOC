from collections import Counter

with open('inputs/input.txt', 'r') as file:
    line: str = file.readline().rstrip('\n')
    list1: list[int] = []
    list2: list[int] = []

    while line:
        l: list[str] = line.split(' ')
        list1.append(int(l[0]))
        list2.append(int(l[-1]))
        line = file.readline().rstrip('\n')
    
    count_dict = Counter(list2)

    similarity = 0
    for k in list1:
        if k in count_dict:
            similarity += (k * count_dict[k])
    
    print(f'Similarity Score: {similarity}')


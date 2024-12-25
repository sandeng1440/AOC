def inputText(file: str) -> list[str]:
    with open(file,'r') as f:
        return f.read().strip().split('\n')

def check_forward(line: str, index: int) -> bool:
    

lines: list[str] = inputText('inputs/test.txt')
count: int = 0

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'X':
            if check_forward(lines[i]):
                count += 1
            if check_right():
                count += 1
            if check_left():
                count += 1
            if check_backward():
                count += 1

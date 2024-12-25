# part 1

# Ans: 472
# Test: 2

def safe(report: list[int]) -> bool:
    z: list[tuple[int,int]] = list(zip(report, report[1:]))
    diffs: list[int] = [x - y for x,y in z]
    asc: bool = all(map(lambda x: x > 0, diffs))
    dsc: bool = all(map(lambda x: x < 0, diffs))
    d: bool = all(map(lambda x: 1 <= abs(x) <= 3, diffs))
    inc_dec: bool = asc or dsc
    if d and inc_dec:
        return True
    return False

if __name__ == '__main__':
    safe_count = 0
    for rep in open('inputs/input.txt', 'r'):
        report = list(map(int, rep.split()))
        if safe(report):
            safe_count += 1

    print(f'Safe Count: {safe_count}')



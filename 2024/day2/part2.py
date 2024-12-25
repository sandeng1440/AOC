# part 2
# problem dampener

# Ans: 520
# Test: 4


def safe(report: list[int]) -> bool:
    z = zip(report, report[1:])
    diffs = [x - y for x,y in z]
    asc = all(map(lambda x: x > 0, diffs))
    dsc = all(map(lambda x: x < 0, diffs))
    d = all(map(lambda x: 1 <= abs(x) <= 3, diffs))
    inc_dec = asc or dsc
    if d and inc_dec:
        return True
    return False

if __name__ == '__main__':
    safe_count = 0
    for rep in open('inputs/input.txt', 'r'):
        report = list(map(int, rep.split()))
        if any(safe(report[:i] + report[i+1:]) for i in range(len(report))):
            safe_count += 1

    print(f'Safe Count: {safe_count}')



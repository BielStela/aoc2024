import re

TEST = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
TEST2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def part1(input: str) -> int:
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    res = 0
    for match in pattern.finditer(input):
        res += int(match.group(1)) * int(match.group(2))

    return res

def part2(input: str) -> int:
    pattern = re.compile(r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)")
    res = 0
    enabled = True
    for match in pattern.finditer(input):
        if "do()" in match.group(0):
            enabled = True
        elif "don't()" in match.group(0):
            enabled = False
        elif "mul" in match.group(0) and enabled:
            res += int(match.group(1)) * int(match.group(2))
    return res



assert part1(TEST) == 161
assert part2(TEST2) == 48, part2(TEST2)

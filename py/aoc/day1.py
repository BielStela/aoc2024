from collections import Counter

TEST = """3   4
4   3
2   5
1   3
3   9
3   3
"""


def parse_input(input: str) -> list[tuple[int, int]]:
    lines = input.strip().split("\n")
    res = []
    for line in lines:
        parts = line.split()
        res.append((int(parts[0]), int(parts[-1])))
    return res


def part1(input: str) -> int:
    pairs = parse_input(input)
    # transpose to get columns
    left_col = sorted(list(zip(*pairs))[0])
    right_col = sorted(list(zip(*pairs))[1])
    return sum(abs(left - right) for left, right in zip(left_col, right_col))


def part2(input: str) -> int:
    pairs = parse_input(input)
    left_col = sorted(list(zip(*pairs))[0])
    right_col = sorted(list(zip(*pairs))[1])
    bag = Counter(right_col)
    return sum(val * bag[val] for val in left_col)


assert part1(TEST) == 11
assert part2(TEST) == 31

import itertools


TEST = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def parse(input: str) -> list[list]:
    return [[int(el) for el in line.split()] for line in input.split("\n") if line]


def is_monotonic(input: list) -> bool:
    return input == sorted(input) or input == sorted(input, reverse=True)


def adjancency_rule(input: list) -> bool:
    sums = [abs(b - a) for a, b in zip(input, input[1:])]
    return all(x >= 1 and x <= 3 for x in sums)


def check_report(report: list[int]) -> bool:
    return is_monotonic(report) and adjancency_rule(report)


def part1(input: str) -> int:
    reports = parse(input)
    results = [check_report(rep) for rep in reports]
    return sum(results)


def part2(input: str) -> int:
    reports = parse(input)
    results = []
    for report in reports:
        if check_report(report):
            results.append(True)
        else:
            passes_with_one_missing = []
            for i in range(len(report)):
                passes_with_one_missing.append(
                    check_report(report[:i] + report[i + 1 :])
                )
            if any(passes_with_one_missing):
                results.append(True)
    return sum(results)


assert part1(TEST) == 2, part1(TEST)
assert part2(TEST) == 4, part2(TEST)

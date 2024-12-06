from collections import Counter
from enum import verify
import itertools
from typing import Iterable


type lines = list[list[str]]


def as_str(i: Iterable) -> str:
    return "".join(i)


def part1(input: str) -> int:
    target = "XMAS"

    lines = [l for l in input.split("\n") if l]
    w, h = len(lines[0]), len(lines)
    flat = list(itertools.chain.from_iterable(lines))

    res = 0
    for y in range(h):
        for x in range(w):
            lookups = []
            if lines[y][x] == "X":
                # look forward
                lookups.append(lines[y][slice(x, x+len(target))])
                # look back
                lookups.append(as_str(reversed(lines[y][slice(x-len(target)+1, x+1)])))
                # look up
                lookups.append(as_str(lines[j][x] for j in range(y, y-len(target), -1) if j >= 0))
                # look down
                lookups.append(as_str(lines[j][x] for j in range(y, y+len(target)) if j < h))
                # up left
                lookups.append(as_str(lines[y - d][x - d] for d in range(0, len(target)) if y - d >= 0 and x - d >= 0))
                # up right
                lookups.append(as_str(lines[y - d][x + d] for d in range(0, len(target)) if (y - d >= 0) and ((x + d) < w)))
                # down left
                lookups.append(as_str(lines[y + d][x - d] for d in range(0, len(target)) if ((y + d) < h) and ((x - d) >= 0)))
                # down right
                lookups.append(as_str(lines[y + d][x + d] for d in range(0, len(target)) if ((y + d) < h) and ((x + d) < w)))
            res += Counter(lookups).get(target, 0)
    return res


def part2(input: str) -> int:
    target = "MAS"

    lines = [l for l in input.split("\n") if l]
    w, h = len(lines[0]), len(lines)

    res = 0
    for y in range(1, h-1):
        for x in range(1, w-1):
            lookups = []
            if lines[y][x] == "A":
                ud = as_str(lines[y - d][x + d] for d in range(-1, 2))
                lookups.append(ud)
                lookups.append(as_str(reversed(ud)))
                du = as_str(lines[y + d][x + d] for d in range(-1, 2))
                lookups.append(du)
                lookups.append(as_str(reversed(du)))
            res += Counter(lookups).get(target, 0) == 2
    return res





TEST="""\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

TEST2= """\
S..S..S
.A.A.A.
..MMM..
SAMXMAS
..MMM..
.A.A.A.
S..S..S
"""

assert part1(TEST) == 18
assert part1(TEST2) == 8, part1(TEST2)
assert part2(TEST) == 9, part2(TEST)

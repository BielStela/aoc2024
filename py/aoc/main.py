from functools import lru_cache
from pathlib import Path

import day1
import day2
import day3

DATA_FOLDER = Path(__file__).parent.parent.parent / "data"


@lru_cache
def get_input(day: str) -> str:
    with open(DATA_FOLDER / day) as f:
        input = f.read()
    return input


def main():
    print("Day1.part1: ", day1.part1(get_input("day1")))
    print("Day1.part2: ", day1.part2(get_input("day1")))
    print("Day2.part1: ", day2.part1(get_input("day2")))
    print("Day2.part2: ", day2.part2(get_input("day2")))
    print("Day3.part1: ", day3.part1(get_input("day3")))
    print("Day3.part2: ", day3.part2(get_input("day3")))


if __name__ == "__main__":
    main()

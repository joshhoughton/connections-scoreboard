from typing import Tuple


def parse_result(message: str) -> Tuple[int, int]:
    lines = message.split("\n")
    puzzle_number = None
    num_lines = 0

    for line in lines:
        if line.startswith("Puzzle #"):
            puzzle_number = int(line.split()[-1])
        elif len(line) == 4:
            num_lines += 1

    return puzzle_number, num_lines

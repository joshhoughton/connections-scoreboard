from typing import Tuple


def parse_result(message: str) -> Tuple[int, int]:
    lines = message.split("\n")
    puzzle_number = None
    attempt_count = 0

    for line in lines:
        if line.startswith("Puzzle #"):
            puzzle_number = int(line.split("#")[-1])
        elif len(line) == 4 and all(c in "🟩🟨🟦🟪" for c in line):
            attempt_count += 1

    return puzzle_number, attempt_count

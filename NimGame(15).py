import math

def minimax(rows, is_max):
    if sum(rows) == 0:
        return -1 if is_max else 1

    scores = []
    for i, p in enumerate(rows):
        for take in range(1, p + 1):
            new_rows = rows[:]
            new_rows[i] -= take
            scores.append(minimax(new_rows, not is_max))

    return max(scores) if is_max else min(scores)

def best_move(rows):
    return max(((i, t) for i, p in enumerate(rows) for t in range(1, p + 1)),
               key=lambda m: minimax([p - (m[1] if i == m[0] else 0) for i, p in enumerate(rows)], False))

def display_rows(rows):
    for i, count in enumerate(rows):
        print(f"Row {i + 1}: {' * ' * count}")

def play_nim():
    rows = [2, 3, 4, 5]
    while sum(rows) > 0:
        display_rows(rows)
        i, take = map(int, input("Select row and how many stones to take: ").split())
        i -= 1  # Adjust for 1-based indexing
        if not (0 <= i < len(rows) and 1 <= take <= rows[i]):
            print("Invalid move!")
            continue
        rows[i] -= take
        if sum(rows) == 0:
            print("You win!"); break
        i, take = best_move(rows)
        print(f"AI removes {take} from row {i + 1}")
        rows[i] -= take
        if sum(rows) == 0:
            print("AI wins!"); break

play_nim()

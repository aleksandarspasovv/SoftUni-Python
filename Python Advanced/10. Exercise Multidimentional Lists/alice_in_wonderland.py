n = int(input())

alice_pos = []
matrix = []
total_tea = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(n):
    matrix.append(input().split())
    if "A" in matrix[row]:
        alice_pos = [row, matrix[row].index("A")]
        matrix[row][alice_pos[1]] = "*"

while total_tea < 10:
    direction = input()
    row = alice_pos[0] + directions[direction][0]
    col = alice_pos[1] + directions[direction][1]
    alice_pos = [row, col]
    element = matrix[row][col]
    matrix[row][col] = '*'

    if element == 'R':
        break
    if element.isdigit():
        total_tea += int(element)


if total_tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
[print(*row) for row in matrix]
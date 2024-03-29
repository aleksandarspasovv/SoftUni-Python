from collections import deque


def fill_the_box(height, length, width, *args):
    size = height * length * width
    cubes = deque(args)

    while cubes[0] != 'Finish':
        size -= cubes.popleft()

        if size < 0:
            cubes_left = sum(x for x in cubes if x != 'Finish')
            return f"No more free space! You have {cubes_left + abs(size)} more cubes."

    return f"There is free space in the box. You could put {size} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
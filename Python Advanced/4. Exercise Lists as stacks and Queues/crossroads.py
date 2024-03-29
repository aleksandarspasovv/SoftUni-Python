from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

command = input()

lane = deque()
total_cars_passed = 0

while True:
    if command == "END":
        print(f"Everyone is safe.")
        print(f"{total_cars_passed} total cars passed the crossroads.")
        break

    elif command == 'green':
        current_green = green_light_duration
        current_free = free_window_duration
        while lane:
            current_car = lane.popleft()
            if len(current_car) < current_green:
                current_green = current_green - len(current_car)
                total_cars_passed += 1
                continue
            elif len(current_car) > current_green:
                total_time = current_green + current_free
                if len(current_car) < total_time:
                    total_cars_passed += 1
                    continue
            elif len(current_car) > current_green + current_free:
                character_hit = len(current_car) - (current_green + current_free)
                print(f'"A crash happened!"')
                print(f"{current_car} was hit at {current_car[::-character_hit]}.")

    else:
        lane.append(command)

    command = input()

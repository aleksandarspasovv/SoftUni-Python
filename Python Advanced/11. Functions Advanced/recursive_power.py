def recursive_power(number, power):
    if power <= 1:
        return 1

    return number * recursive_power(number, power - 1)


print(recursive_power(10, 100))
print(recursive_power(2, 10))

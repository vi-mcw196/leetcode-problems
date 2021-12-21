def is_power_of_two(n: int) -> bool:
    return not n & n - 1 if n else False


print(is_power_of_two(8))

# https://www.ritambhara.in/check-if-number-is-a-power-of-2/ <------- useful link

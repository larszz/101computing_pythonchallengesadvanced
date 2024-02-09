import random

goat = "goat"
car = "car"


def get_doors() -> list[str]:
    doors = [goat, goat, car]
    random.shuffle(doors)
    return doors


def get_goat_door_index(doors: list[str], chosen: int) -> int:
    options = [_ for _ in range(len(doors))]
    # remove "car door"
    for i in range(len(doors)):
        if doors[i] == car:
            options.pop(i)
    # remove chosen
    if chosen in options:
        options.remove(chosen)
    return random.choice(options)


def is_winning_door(doors: list[str], chosen: int) -> bool:
    return doors[chosen] == car


def play(switch: bool) -> bool:
    options = [_ for _ in range(3)]
    doors = get_doors()
    # decide which door to pick
    decision = random.choice(options)
    # reveal goat door
    goat_door_index = get_goat_door_index(doors, decision)

    if switch:
        options.remove(decision)
        options.remove(goat_door_index)
        return is_winning_door(doors, options[0])
    else:
        return is_winning_door(doors, decision)


number_of_times_per_switch_option = 500
if __name__ == '__main__':
    result: list[list[int]] = [[0, 0], [0, 0]]

    for switch in [True, False]:
        for i in range(number_of_times_per_switch_option):
            switch_idx = 0 if switch else 1
            if play(switch):
                result[switch_idx][0] += 1
            else:
                result[switch_idx][1] += 1


    seperator = "--------------------------------------------------"
    print(f"Statistic after {2 * number_of_times_per_switch_option} attempts: ")
    print(seperator)
    print(f"SWITCHING")
    print(f"Wins:   {result[0][0]}")
    print(f"Losses: {result[0][1]}")
    print(f"NOT SWITCHING")
    print(f"Wins:   {result[1][0]}")
    print(f"Losses: {result[1][1]}")


def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    return [badge_maker(name) for name in names]


def assign_rooms(names):
    rooms = []
    for i in range(0, 8):
        rooms.append(f"Hello, {names[i]}! You'll be assigned to room {i+1}!")
    return rooms


def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for room in assign_rooms(names):
        print(room)
    return None

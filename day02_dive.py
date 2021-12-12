with open('input/dive.txt') as f:
    instructions = [line.rstrip() for line in f]

#print(instructions)

def naive(instructions):
    horizontal_tot, depth_tot = 0, 0

    for order in instructions:
        direction, val = order.split()
        if direction == 'forward':
            horizontal_tot += int(val)
        elif direction == 'up':
            depth_tot -= int(val)
        elif direction == 'down':
            depth_tot += int(val)

    print(horizontal_tot,depth_tot,horizontal_tot*depth_tot)

def sophisticated(instructions):
    aim, horizontal_tot, depth_tot = 0, 0, 0

    for order in instructions:
        direction, val = order.split()
        if direction == 'forward':
            horizontal_tot += int(val)
            depth_tot += int(val) * aim
        elif direction == 'up':
            aim -= int(val)
        elif direction == 'down':
            aim += int(val)

    print(horizontal_tot,depth_tot,horizontal_tot*depth_tot)

sophisticated(instructions)
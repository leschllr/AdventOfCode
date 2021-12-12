with open('input/hydrothermalventure.txt') as f:
    segments = [line.rstrip() for line in f]

coordinates = []

for line in segments:
    pos = line.find('->')
    begin = [int(a) for a in line[:pos].split(',')]
    end = [int(a) for a in line[pos+2:].split(',')]
    coordinates.append([begin,end])
    
hor_vert = []
diagonals = []
x_min,x_max,y_min,y_max = 1000,0,1000,0

for line in coordinates:
    begin,end = line[0],line[1]
    if begin[0] < x_min or end[0] < x_min:
        x_min = min(begin[0],end[0])
    if begin[0] > x_max or end[0] > x_max:
        x_max = max(begin[0],end[0])
    if begin[1] < y_min or end[1] < y_min:
        y_min = min(begin[1],end[1])
    if begin[1] > y_max or end[1] > y_max:
        y_max = max(begin[1],end[1])

    if begin[0] == end[0] or begin[1] == end[1]:
        hor_vert.append(line)
    elif abs(begin[0]-end[0]) == abs(begin[1]-end[1]):
        diagonals.append(line)

#print(x_min,x_max,y_min,y_max)
#print(hor_vert)
#print(diagonals)
#print(len(hor_vert))

def all_points_between(begin,end):
    point_list = []

    begin_x = begin[0]
    begin_y = begin[1]
    end_x = end[0]
    end_y = end[1]

    for i in range(min(begin_x,end_x),(max(begin_x,end_x) + 1 )):
        for j in range(min(begin_y,end_y),(max(begin_y,end_y) + 1 )):
            point_list.append([i,j])
    return point_list

def diagonal_between(begin,end):
    point_list = []

    begin_x = begin[0]
    begin_y = begin[1]
    end_x = end[0]
    end_y = end[1]

    low_x = min(begin_x,end_x)
    high_x = max(begin_x,end_x)

    for i,val in enumerate(range(low_x,(high_x + 1))):
        if begin_x == high_x and begin_y == max(begin_y,end_y):
            point_list.append([val,(end_y+i)])
        elif begin_x == high_x and begin_y == min(begin_y,end_y):
            point_list.append([val,(end_y-i)])
        elif begin_x == low_x and begin_y == min(begin_y,end_y):
            point_list.append([val,(begin_y+i)])
        elif begin_x == low_x and begin_y == max(begin_y,end_y):
            point_list.append([val,(begin_y-i)])

    return point_list


grid = [[0] * (x_max - x_min + 1) for _ in range (y_max - y_min + 1)]

for line in hor_vert:
    begin,end = line[0],line[1]
    point_list = all_points_between(begin,end)
    for point in point_list:
        x = point[0]
        y = point[1]
        grid[y-y_min][x-x_min] += 1

for line in diagonals:
    begin,end = line[0],line[1]
    point_list = diagonal_between(begin,end)
    for point in point_list:
        x = point[0]
        y = point[1]
        grid[y-y_min][x-x_min] += 1

critical = 0

#for line in grid:
#    print(line)

for row in grid:
    for col in row:
        if col >= 2:
            critical += 1

print(critical)
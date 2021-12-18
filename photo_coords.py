import math

def find_coordinates(square_coordinates, h_min: float) -> list:
    degree_x = (53.5 * math.pi) / 180
    degree_y = (41.41 * math.pi) / 180

    coor_1 = square_coordinates[0]
    coor_2 = square_coordinates[1]
    coor_3 = square_coordinates[2]
    coor_4 = square_coordinates[3]

    side_x = distance(coor_1, coor_4)
    
    h = (2 * side_x) / math.tan(degree_x / 2)

    i = 1
    while (h/i > h_min):
        i += 1
    if i == 1:
        drone_height = h
    else: drone_height = h / (i - 1)

    step_x = 2 * drone_height * math.tan(degree_x / 2)
    step_y = 2 * drone_height * math.tan(degree_y / 2)
    foto_coordinates = list()

    to = False
    current_loc = (coor_1[0] - step_x / 2, coor_1[1] + step_y / 2)
    while (current_loc[0] + step_x / 2 < coor_4[0]):
        current_loc = (current_loc[0] + step_x, current_loc[1])
        foto_coordinates.append(current_loc)
        if to:
            while(current_loc[1] - step_y / 2 > coor_4[1]):
                current_loc = (current_loc[0], current_loc[1] - step_y)
                foto_coordinates.append(current_loc)
            to = False
        else:
            while(current_loc[1] + step_y / 2 < coor_2[1]):
                current_loc = (current_loc[0], current_loc[1] + step_y)
                foto_coordinates.append(current_loc)
            to = True

    return foto_coordinates


def distance(coor_1: tuple, coor_2: tuple) -> float:
    return math.sqrt( (coor_1[0] - coor_2[0]) ** 2 + (coor_1[1] - coor_2[1]) ** 2 )


# print(len(find_coordinates([(0, 0), (0, 100), (100, 100), (100, 0)], 1)))
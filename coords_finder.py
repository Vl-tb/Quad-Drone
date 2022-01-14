from math import tan, pi, ceil
from copy import deepcopy

def center(vert_1, vert_2, vert_3):
    c_vert = ((vert_2[0] + vert_3[0])/2, (vert_2[1] + vert_3[1])/2)

    vert_4 = (c_vert[0]*2 - vert_1[0], c_vert[1]*2 - vert_1[1])

    return c_vert, vert_4

def distance(point_1, point_2):
    return ((point_1[0]-point_2[0])**2 + (point_1[1]-point_2[1])**2)**0.5

def new_edge(point_1, point_2, side_a):
    try:
        k = (point_1[1] - point_2[1])/(point_1[0] - point_2[0])
        b = point_2[1] - k*point_2[0]
        D = (2*k*b - 2*point_1[1]*k)**2 - 4*(1+k**2)*(point_1[0]**2 +
                point_1[1]**2 + b**2 - side_a**2 - 2*point_1[1]*b)

        x_1 = ((2*point_1[1]*k-2*k*b) + D**0.5)/(2*(1 + k**2))
        x_2 = ((2*point_1[1]*k-2*k*b) - D**0.5)/(2*(1 + k**2))
        y_1 = k*x_1 + b
        y_2 = k*x_2 + b

        if (distance(point_2, (x_1, y_1)) < distance(point_2, (x_2, y_2))):
            return (x_1, y_1)
        return (x_2, y_2)
    except ZeroDivisionError:
        if point_2[1] - point_1[0] > 0:
            return (point_1[0], point_1[1]+side_a)
        else:
            return (point_1[0], point_1[1]-side_a)


def find_center(edge_1, edge_2, edge_3, min_high):
    side_a = distance(edge_1, edge_2)
    side_b = distance(edge_1, edge_3)

    degree_x = (53.5 * pi) / 180
    degree_y = (41.41 * pi) / 180

    a = min_high*tan(degree_x/2)
    b = min_high*tan(degree_y/2)

    sections_x = ceil(side_a/a)
    sections_y = ceil(side_b/b)

    side_a = sections_x*a
    side_b = sections_y*b

    edge_2 = new_edge(edge_1, edge_2, side_a)
    edge_3 = new_edge(edge_1, edge_3, side_b)

    coords = []

    for i in range(sections_y):
        row = []
        lamb_1 = 1/(sections_x-1)
        try:
            lamb_2 = (i+1)/(sections_y-i-1)
            left_down = ((edge_1[0] + lamb_2*edge_3[0])/(1 + lamb_2), (edge_1[1] + lamb_2*edge_3[1])/(1 + lamb_2))
        except ZeroDivisionError:
            left_down = edge_3
        left_up = edge_1
        right_up = ((edge_1[0] + lamb_1*edge_2[0])/(1 + lamb_1), (edge_1[1] + lamb_1*edge_2[1])/(1 + lamb_1))
        
        for j in range(sections_x):
            verts = center(left_up, right_up, left_down)
            row.append(verts[0])
            left_up = deepcopy(right_up)
            left_down = verts[1]
            try:
                right_up = ((edge_1[0] + ((j+2)/(sections_x-j-2))*edge_2[0])/(1 + 
                    ((j+2)/(sections_x-j-2))), (edge_1[1] + 
                    ((j+2)/(sections_x-j-2))*edge_2[1])/(1 + ((j+2)/(sections_x-j-2))))
            except ZeroDivisionError:
                right_up = edge_2
        edge_2 = verts[1]
        edge_1 = ((edge_1[0] + lamb_2*edge_3[0])/(1 + lamb_2), (edge_1[1] + lamb_2*edge_3[1])/(1 + lamb_2))
        coords.append(row)
    return coords

if __name__ == "__main__":
    print(find_center((0, 100), (100, 100), (0, 0), 80))
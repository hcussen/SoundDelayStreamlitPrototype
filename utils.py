import math


def distance_to_box(marcher_x, marcher_y, box_y, box_z):
    del_x = marcher_x
    del_y = abs(marcher_y) + abs(box_y)
    del_z = box_z

    return math.sqrt(del_x ** 2 + del_y ** 2 + del_z ** 2)

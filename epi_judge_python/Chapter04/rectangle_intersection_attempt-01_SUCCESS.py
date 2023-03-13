import collections
import math

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    target = Rect(0, 0, -1, -1)
    x1, x2 = find_intersection_rect_coords_x_axis(r1, r2)
    y1, y2 = find_intersection_rect_coords_y_axis(r1, r2)

    if x1 < math.inf and y1 < math.inf:
        width = abs(x1 - x2)
        height = abs(y1 - y2)
        target = Rect(x1, y1, width, height)

    return target


def find_intersection_rect_coords_x_axis(lower_rect: Rect, other_rectangle: Rect):
    if lower_rect.x > other_rectangle.x:
        return find_intersection_rect_coords_x_axis(other_rectangle, lower_rect)

    r_lower_start = lower_rect.x
    r_lower_finish = r_lower_start + lower_rect.width
    r_other_start = other_rectangle.x
    r_other_finish = r_other_start + other_rectangle.width

    # If the other rectangle starts before the lower rectangle finishes
    if r_other_start <= r_lower_finish:
        return r_other_start, min(r_lower_finish, r_other_finish)

    return math.inf, math.inf


def find_intersection_rect_coords_y_axis(lower_rect: Rect, other_rectangle: Rect):
    if lower_rect.y > other_rectangle.y:
        return find_intersection_rect_coords_y_axis(other_rectangle, lower_rect)

    r_lower_start = lower_rect.y
    r_lower_finish = r_lower_start + lower_rect.height
    r_other_start = other_rectangle.y
    r_other_finish = r_other_start + other_rectangle.height

    # If the other rectangle starts before the lower rectangle finishes
    if r_other_start <= r_lower_finish:
        return r_other_start, min(r_lower_finish, r_other_finish)

    return math.inf, math.inf


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))

# find the least sum path from top left to bottom right
# and you can only move down and right.

single_arr = [1]
two_dimensional_arr = [[2, 3], [1, 2]]


def least_sum_route(single_arr):
    pass


# TESTS

# first test reduce to single cell and this is base case?
# If len(list) == 1: return list
def test_single_cell():
    assert least_sum_route(single_arr) == [1]

# find the least sum path from top left to bottom right
# and you can only move down and right.

single_arr = [1]
four_arr = [[1,8], [2, 3]]
# two_dimensional_arr = [[2, 3], [1, 2]]


def least_sum_route(arr):
    # base case
    if len(single_arr) == 1:
        return single_arr
    # recursive case


'''   TESTS   '''
# first test reduce to single cell and this is base case?
# If len(list) == 1: return list
def test_single_cell():
    assert least_sum_route(single_arr) == [1]


def test_four_cell():
    assert least_sum_route(four_arr) == 6

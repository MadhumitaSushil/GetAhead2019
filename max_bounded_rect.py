"""
Given an array of non-negative integers that represent the bars (y value) in a histogram (with the array index being the x value), find the rectangle with the largest area under the curve and above the x-axis (i.e. the largest rectangle that fits inside the histogram). Return the pair of array indices that represent the rectangle.

Test Cases
Note that there may be other valid answers.
For array [2,4,2,1], the largest area is 6, with height 2, and width from indices 0 to 2:
For array [2,4,2,1,10,6,10] the largest area is 18, with height 6 and width from indices 4 to 6.
"""

def get_max_bounded_rect(heights):
    """
    Brute force solution O(n^2)

    I am certain that a DP solution in O(n) is possible,
    but I was not succesful in arriving at the correct solution.
    I was trying to use stacks by pushing indices and storing all elements greater than current element,
    so that we iterate just once. If this condition becomes false, we pop the element and compute area.
    However, I was still confused about how to do it for all element combinations.
    Do we push the remaining elements back and repeat? But that increases complexity again.
    I could not figure out this part.

    :param heights: array-like object of y-axis
    :return: start and end index of the largest rectangle (inclusive)
    """

    if len(heights) == 0 or not heights:
        raise ValueError("Empty input")

    max_area = 0
    start_idx = 0
    end_idx = 0

    for i, cur_ht in enumerate(heights):

        # check right elements if indices are within rectangle bounds
        j = i + 1
        while j < len(heights) and heights[j] >= cur_ht:
            j += 1

        # check left elements if they lie within bounds
        k = i - 1
        while k >= 0 and heights[k] >= cur_ht:
            k -= 1

        # calculate area
        cur_area = (j - (k+1)) * cur_ht

        # update area, indices
        if cur_area > max_area:
            max_area = cur_area
            start_idx = k+1
            end_idx = j-1

    print("Max area: {}, start_idx(inclusive): {}, end_idx (inclusive): {} "
          .format(max_area, start_idx, end_idx))
    return start_idx, end_idx


if __name__ == '__main__':

    assert(get_max_bounded_rect([2, 4, 2, 1]) == (0, 2))

    assert(get_max_bounded_rect([2, 4, 2, 1, 10, 6, 10]) == (4, 6))

    assert(get_max_bounded_rect([1]) == (0, 0))








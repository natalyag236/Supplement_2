def area (length, width):
    """ calculate the area of a rectangle.
    Args:
        lenght: the length of the rectangle
        width: the width of the rectangle.
    Returns:
        the calculated area of the rectangle.
    """
    return length * width

def test_calculate_rectangle_area():
    assert area (5,6) == 30
    
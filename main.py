import math
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

def triangle_area(base, height):
    """
    calculate the area of a triangle

    Args:
        base: the base of the triangle
        height: the height of the triangle.
    Returns:
        the calculated area of the 
    """
    return base * height / 2

def test_calculate_triangle_area():
    assert triangle_area (10,12) == 60.0

def circle_area(radius):
    """ 
    Calculate the area of a circle given its radius

        Args:
            radius: the radius of the circle
        
        Returns:
            the area of the circle
    """
    return math.pi * (radius ** 2)

def test_circle_area():
    radius = 3
    circ_area = 28.27433
    assert round(circle_area(radius),5) == round(circ_area,5)
import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14


def test_multiplication():
    output = methods.multiplication(1,1)
    assert output == 1

def test_sum():
    output = methods.sum(1,2)
    assert output == 3

def test_division():
    output = methods.division(81, 9)
    assert output == 9

def test_sub():
    output = methods.sub(100,9)
    assert output == 91
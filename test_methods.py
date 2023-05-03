import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 10
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 50
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 10
    height = 10

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 40

def test_soma():
    x = 25
    y = 25

    output = methods.som(x, y)

    assert output == 50

def test_sub():
    x = 20
    y = 15

    output = methods.sub(x, y)

    assert output == 5

def test_mult():
    x = 5
    y = 5

    output = methods.mult(x, y)

    assert output == 25

def test_div():
    x = 20
    y = 10

    output = methods.div(x, y)

    assert output == 2
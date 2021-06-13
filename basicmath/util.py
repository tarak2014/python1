def add_num(first_no, second_no):
    return first_no + second_no

def sub_num(first_no, second_no):
    return first_no - second_no

def mul_num(first_no, second_no):
    return first_no * second_no

def div_num(first_no, second_no):
    return first_no / second_no


def test_add_num():
    assert add_num(3,4) == 7

def test_sub_num():
    assert sub_num(3,4) == -1

def test_mul_num():
    assert mul_num(3,4) == 12

def test_div_num():
    assert div_num(3,4) == 0.75

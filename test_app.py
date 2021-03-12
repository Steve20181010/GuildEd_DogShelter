# test_app.py

import pytest
from calc_dogfood_supply import validate_input, calc_order_quantity


# test data input validation....
def test_valid_maxdogs_entry():
    # Test Max Dogs equal max 30
    test_list = [1, 26, 3, 4.6]
    msg = validate_input(test_list[0], test_list[1], test_list[2])
    assert msg == ''


def test_negative_s_dog_entry():
    # Test Small Dog < 0
    test_list = [-1, 2, 3, 4.6]
    msg = validate_input(test_list[0], test_list[1], test_list[2])
    assert msg == 'Dog numbers cannot be negative numbers'


def test_negative_m_dog_entry():
    # Test Medium Dog < 0
    test_list = [1, -2, 3, 4.6]
    msg = validate_input(test_list[0], test_list[1], test_list[2])
    assert msg == 'Dog numbers cannot be negative numbers'


def test_negative_l_dog_entry():
    # Test Large Dog < 0
    test_list = [1, 2, -3, 4.6]
    msg = validate_input(test_list[0], test_list[1], test_list[2])
    assert msg == 'Dog numbers cannot be negative numbers'


def test_invalid_maxdogs_entry():
    # Test Max Dogs greater than 30
    test_list = [1, 26, 4, 4.6]
    msg = validate_input(test_list[0], test_list[1], test_list[2])
    assert msg != ''


def test_lower_maxdogs_entry():
    # Test Max Dogs equal 0
    test_list = [0, 0, 0, 4.6]
    msg = validate_input(test_list[0], test_list[1], test_list[2])
    assert msg == ''


def test_large_maxdogs_entry():
    # Test Max Dogs way large
    test_list = [999999, 999999, 999999, 4.6]
    msg = validate_input(test_list[0], test_list[1], test_list[2])
    assert msg != ''


def test_raises_small_dog_exception_on_non_int_argument():
    with pytest.raises(ValueError):
        # Test Invalid Smll Dogs entry (entered string)
        test_list = ['Small', 9, 10, 4.6]
        msg = validate_input(test_list[0], test_list[1], test_list[2])
        print('msg={}'.format(msg))


def test_raises_med_dog_exception_on_non_int_argument():
    with pytest.raises(ValueError):
        # Test Invalid Med Dogs entry (entered string)
        test_list = [1, 'medium', 10, 4.6]
        msg = validate_input(test_list[0], test_list[1], test_list[2])
        print('msg={}'.format(msg))


def test_raises_big_dog_exception_on_non_int_argument():
    with pytest.raises(ValueError):
        # Test Invalid Big Dogs entry (entered string)
        test_list = [1, 2, 'BIG', 4.6]
        msg = validate_input(test_list[0], test_list[1], test_list[2])


# test calc_order_quantity...
def test_entry_calc():
    # Test order quantity equal 363.6
    test_list = [5, 3, 7, 17]
    result_amt = calc_order_quantity(test_list[0], test_list[1], test_list[2], test_list[3])
    assert result_amt == 363.6


def test_entry_calc2():
    # Test order quantity equal 1059.6
    test_list = [0, 0, 30, 17.998]
    result_amt = calc_order_quantity(test_list[0], test_list[1], test_list[2], test_list[3])
    assert result_amt == 1059.6


def test_entry_calc3():
    # Test 0 dog minimum, order quantity is negative and equal to -20.4
    test_list = [0, 0, 0, 17]
    result_amt = calc_order_quantity(test_list[0], test_list[1], test_list[2], test_list[3])
    assert result_amt == -20.4


def test_entry_calc4():
    # Test 30 dog max, order quantity equal 630.0
    test_list = [10, 10, 10, 17]
    result_amt = calc_order_quantity(test_list[0], test_list[1], test_list[2], test_list[3])
    assert result_amt == 699.6

import codewars_test as test
from solution import quarter_of

@test.describe("Fixed Tests")
def basic_tests():
    test.assert_equals(quarter_of(3), 1)
    test.assert_equals(quarter_of(8), 3)
    test.assert_equals(quarter_of(11), 4)
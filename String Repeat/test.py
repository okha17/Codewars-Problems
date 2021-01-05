@test.describe('Fixed tests')
def basic_tests():
    test.assert_equals(repeat_str(4, 'a'), 'aaaa')
    test.assert_equals(repeat_str(3, 'hello '), 'hello hello hello ')
    test.assert_equals(repeat_str(2, 'abc'), 'abcabc')
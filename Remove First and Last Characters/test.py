@test.describe("Sample Tests")
def basic_tests():
    test.assert_equals(remove_char('eloquent'), 'loquen')
    test.assert_equals(remove_char('country'), 'ountr')
    test.assert_equals(remove_char('person'), 'erso')
    test.assert_equals(remove_char('place'), 'lac')
    test.assert_equals(remove_char('ok'), '')
    test.assert_equals(remove_char('ooopsss'), 'oopss')
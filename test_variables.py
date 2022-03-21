import variables
import unittest
from ddt import ddt, data

class Test_TestTask1(unittest.TestCase):
    def test_integer(self):
        #self.assertEqual(variables.task1(3, 4), 7)
        self.assertEqual(variables.task1(4, 5), 9)
        self.assertEqual(variables.task1(2, 3), 5)

    def test_float(self):
        self.assertEqual(type(variables.task1(5.0, 3.0)), int)

    def test_string(self):
        self.assertEqual(type(variables.task1("5", "3")), int)

    def test_string_number(self):
        self.assertEqual(variables.task1("5", "3"), 8)

class Test_TestDzielenie(unittest.TestCase):
    def test_dividezeroError(self):
        with self.assertRaises(ZeroDivisionError):
            variables.dzielenie(5,0)

@ddt
class Test_TestTask2(unittest.TestCase):
    @data((2, 4), (5, 25),(6,36))
    def test_integer(self, value):
        input, output = value
        self.assertEqual(variables.task2(input), output)

    def test_doc(self):
        self.assertTrue("Input" in variables.task2.__doc__)

class TestTask(unittest.TestCase):
    """
    Write some test for variables, text_operation or coleection module (rememmber to change name)
    Try to crash it and improve a little bit, use parametrization with other arguments (like strings)
    """
    pass

if __name__ == '__main__':
    unittest.main()
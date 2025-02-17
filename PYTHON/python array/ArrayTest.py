import unittest
from Arrays import *
array = Arrays(5,str)
class MyTestCase(unittest.TestCase):
    def test_if_array_is_created(self):
        array1 = Arrays(5,str)

    def test_if_insert_element_exists(self):
        array.insert(2, "manny")

    def test_if_instert_raise_typeerror_exception(self):
        self.assertRaises(TypeError, array.insert,2, 78)

    def test_if_insert_raise_IndexError_exception(self):

        self.assertRaises(IndexError, array.insert,6, "monkey")

    def test_if_insert_adds_element_to_array_of_given_index(self):
        array.insert(2, "manny")

    def test_if_delete_method_exists(self):
        array.delete(2)

    def test_if_delete_method_raise_indexerror_exception(self):
        self.assertRaises(IndexError, array.delete, 6)



if __name__ == '__main__':
    unittest.main()

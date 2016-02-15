# I'm sure that this is not good practice; I've come across using setuptools / setup.py to do a local dev install
# (e.g. http://stackoverflow.com/questions/1893598/pythonpath-vs-sys-path), but I just don't have the time to figure
# out the intricacies of that mechanism, so proper deployment will have to fall to the wayside for now.
import sys
import os
import unittest

sys.path.insert(1, os.getcwd())
from scrapymasters.util.StringUtil import StringUtil


class StringUtilTest(unittest.TestCase):
    def test_get_first_should_return_first_item_in_nonempty_list(self):
        list_input = ["a", "b", "c"]

        result = StringUtil.get_first(list_input, "d")

        self.assertEqual(result, "a")

    def test_get_first_should_return_second_argument_in_empty_list(self):
        list_input = []

        result = StringUtil.get_first(list_input, "d")

        self.assertEqual(result, "d")


    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')
        #
        # def test_isupper(self):
        #     self.assertTrue('FOO'.isupper())
        #     self.assertFalse('Foo'.isupper())
        #
        # def test_split(self):
        #     s = 'hello world'
        #     self.assertEqual(s.split(), ['hello', 'world'])
        #     # check that s.split fails when the separator is not a string
        #     with self.assertRaises(TypeError):
        #         s.split(2)


if __name__ == '__main__':
    unittest.main()

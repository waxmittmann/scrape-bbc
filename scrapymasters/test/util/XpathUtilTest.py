# I'm sure that this is not good practice; I've come across using setuptools / setup.py to do a local dev install
# (e.g. http://stackoverflow.com/questions/1893598/pythonpath-vs-sys-path), but I just don't have the time to figure
# out the intricacies of that mechanism, so proper deployment will have to fall to the wayside for now.
import sys
import os
import unittest

sys.path.insert(1, os.getcwd())
from scrapymasters.util.XPathUtil import XpathUtil


class XpathUtilTest(unittest.TestCase):
    def test_xpath_for_class_should_return_correct_xpath_statement_to_match_class(self):
        result = XpathUtil.xpath_for_class("someclass")

        self.assertEqual(result, "*[contains(concat(' ', @class, ' '), ' someclass ')]")

    if __name__ == '__main__':
        unittest.main()

# I'm sure that this is not good practice; I've come across using setuptools / setup.py to do a local dev install
# (e.g. http://stackoverflow.com/questions/1893598/pythonpath-vs-sys-path), but I just don't have the time to figure
# out the intricacies of that mechanism, so proper deployment will have to fall to the wayside for now.
import sys
import os
import unittest

sys.path.insert(1, os.getcwd())
from scrapymasters.test.StringUtilTest import StringUtilTest
from scrapymasters.test.XpathUtilTest import XpathUtilTest


class TestSuite(unittest.TestCase):
    if __name__ == '__main__':
        # suite = unittest.TestLoader()\
        #     .loadTestsFromTestCase(StringUtilTest)\
        #     .loadTestsFromTestCase(XpathUtilTest)

        # suite = unittest.TestLoader()._find_tests(".", "*Test.py").
        # suite = unittest.TestLoader().loadTestsFromModule("scrapymasters.test")
        suite = unittest.TestLoader().discover(".", pattern='*Test.py', top_level_dir=None)
        unittest.TextTestRunner(verbosity=2).run(suite)

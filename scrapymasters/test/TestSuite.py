import unittest


class TestSuite(unittest.TestCase):
    if __name__ == '__main__':
        # suite = unittest.TestLoader()\
        #     .loadTestsFromTestCase(StringUtilTest)\
        #     .loadTestsFromTestCase(XpathUtilTest)

        # suite = unittest.TestLoader()._find_tests(".", "*Test.py").
        # suite = unittest.TestLoader().loadTestsFromModule("scrapymasters.test")
        suite = unittest.TestLoader().discover(".", pattern='*Test.py', top_level_dir=None)
        unittest.TextTestRunner(verbosity=2).run(suite)

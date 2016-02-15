import unittest


class TestSuite(unittest.TestCase):
    if __name__ == '__main__':
        suite = unittest.TestLoader().discover(".", pattern='*Test.py', top_level_dir=None)
        unittest.TextTestRunner(verbosity=2).run(suite)

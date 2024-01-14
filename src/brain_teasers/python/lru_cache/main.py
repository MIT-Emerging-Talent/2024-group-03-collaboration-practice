import unittest


def run_tests():
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='tests', pattern='test_*.py')

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    run_tests()

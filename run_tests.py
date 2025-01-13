import unittest
import sys
import os

def run_tests():
    # Mengambil direktori tests
    test_dir = os.path.join(os.path.dirname(__file__), 'tests')
    
    # Load semua test
    loader = unittest.TestLoader()
    suite = loader.discover(test_dir, pattern='test_*.py')
    
    # Menjalankan test dengan reporting
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    run_tests()
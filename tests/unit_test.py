import dataclasses
import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal # <-- for testing dataframes

class DFTests(unittest.TestCase):

    """ class for running unittests """

    def setUp(self):
        """ Your setUp """
        TEST_INPUT_DIR = 'data/'
        test_file_name =  'testdata.csv'
        try:
            data = pd.read_csv(INPUT_DIR + test_file_name,
                sep = ',',
                header = 0)
        except IOError:
            print('cannot open file')
        self.fixture = dataclasses

    def test_dataFrame_constructedAsExpected(self):
        """ Test that the dataframe read in equals what you expect"""
        foo = pd.DataFrame()
        assert_frame_equal(self.fixture, foo)

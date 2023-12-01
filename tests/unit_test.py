import pandas as pd


def setUpModule():
    global df 
    df = pd.read_csv('movies.csv')


class TestData():
    @dt.mandatory
    def test_columns(self):
        self.assertValid(
            df.columns,
            {'title', 'rating', 'year', 'runtime'},
        )
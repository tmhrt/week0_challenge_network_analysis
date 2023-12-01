from defusedxml import DTDForbidden
import pandas as pd


def setUpModule():
    global df 
    df = pd.read_csv('movies.csv')


class TestData():
    @DTDForbidden.mandatory # type: ignore
    def test_columns(self):
        self.assertValid( # type: ignore
            df.columns,
            {'title', 'rating', 'year', 'runtime'},
        )
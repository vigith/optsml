import os
import unittest
import pandas as pd

from optsml.tools.data_parser import JSONDataParser


class TestJSONDataParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.abs_file_path = os.path.dirname(__file__)
        cls.parser = JSONDataParser(os.path.join(cls.abs_file_path, '../testdata/test_data.json'))

    def test_read(self):
        df = self.parser.read()
        print(df)

        self.assertIsInstance(df, pd.DataFrame)

    def test_save_to_csv(self):
        self.parser.save_as_csv(os.path.join(self.abs_file_path, '../testdata/test_csv.csv'))


if __name__ == '__main__':
    unittest.main()

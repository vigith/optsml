import pandas as pd


class JSONDataParser:
    """
    Parser for JSON testdata.
    """
    def __init__(self, file_dir: str):
        self.file_dir = file_dir

    def read(self) -> pd.DataFrame:
        df = pd.read_json(self.file_dir, lines=True)
        return df

    def stream(self):
        pass

    def save_as_csv(self, output_file: str) -> None:
        dframe = self.read()
        dframe.to_csv(output_file, index=False)

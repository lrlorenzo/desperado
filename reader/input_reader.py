import pandas as pd

class InputReader:
    def __init__(self, file_path, header, dtypes=None, parse_dates=None):
        self.file_path = file_path
        self.header = header
        self.dtypes = dtypes
        self.parse_dates = parse_dates

    def read(self):
        df = pd.read_excel(self.file_path, 
                           names=self.header,
                           dtype=self.dtypes, 
                           parse_dates=self.parse_dates).fillna("")
        return df
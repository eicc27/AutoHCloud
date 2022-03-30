import pandas as pd


class PersonalInfoReader:
    """
    Reads the formatted xlsx using pandas.
    """
    def __init__(self, path: str) -> None:
        self.df = pd.read_excel(path)
    
    def get_rows(self) -> list[list[str]]:
        res = []
        for _, info in self.df.iterrows():
            row = []
            for i in info:
                row.append(i)
            res.append([row[2], row[1], row[3], str(row[6]) if str(row[6]) != "nan" else ""])
        return res[1:]
    

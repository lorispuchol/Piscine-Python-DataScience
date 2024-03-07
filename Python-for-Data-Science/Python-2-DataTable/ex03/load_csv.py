import pandas as pd


# (You have to adapt the type of return according to your library)
def load(path: str, fields) -> pd.DataFrame:
    '''return content of csv file as DataFrame'''
    try:
        df = pd.read_csv(path, skipinitialspace=True, usecols=fields)
        print("Loading dataset of dimensions", df.shape)
        return df
    except BaseException as e:
        print("MyError", e)
        return None

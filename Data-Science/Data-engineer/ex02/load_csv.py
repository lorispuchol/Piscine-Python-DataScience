import pandas as pd


# (You have to adapt the type of return according to your library)
def load(path: str) -> pd.DataFrame:
    '''return content of csv file as DataFrame'''
    try:
        df = pd.read_csv(path)
        print("Loading dataset of dimensions", df.shape)
        return df
    except BaseException as e:
        print("Error:", e)
        return None

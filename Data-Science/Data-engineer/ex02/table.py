from load_csv import load
from sqlalchemy import create_engine


def main():
    """display life expectancy of France"""
    try:
        df = load("../../data/customer/data_2022_oct.csv")
        if df is None:
            raise BaseException("A porbleme occured to load file")

        conn_string = "postgresql://lpuchol:mysecretpassword@localhost:5432/piscineds"

        db = create_engine(conn_string)
        df.to_sql("table", db)

    except BaseException as e:
        print("Error:", e)


if __name__ == "__main__":
    main()

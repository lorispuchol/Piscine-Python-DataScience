from load_csv import load
import matplotlib.pyplot as plt


def main():
    '''display life expectancy of France'''

    try:

        df = load("../life_expectancy_years.csv")
        if df is None:
            raise BaseException("A porbleme occured to load file")

        france = df[df['country'] == 'France']
        x = france.columns[1:].values.astype(int)
        y = france.iloc[0, 1:].values

        plt.plot(x, y)

        plt.title("France Life Expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")

        plt.show()

    except BaseException as e:
        print("MyError", e)


if __name__ == "__main__":
    main()

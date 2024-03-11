from load_csv import load
import matplotlib.pyplot as plt


def decode_value(s: str):
    """Change M and k data string to the good float data"""
    if "M" in s:
        return float(s.replace("M", "")) * 1000000
    if "k" in s:
        return float(s.replace("k", "")) * 1000
    return float(s)


def main():
    '''Display graph of Belgium and France population'''
    try:
        df = load("../population_total.csv")
        if df is None:
            raise BaseException("A porbleme occured to load file")
        x = df.columns[1:].values.astype(int)

        year = x[:250]

        france = df[df["country"] == "France"]
        belgium = df[df["country"] == "Belgium"]

        y1 = france.iloc[0, 1:].values
        y2 = belgium.iloc[0, 1:].values

        y1 = [decode_value(item) for item in y1]
        y2 = [decode_value(item) for item in y2]
        y = [y1[:250], y2[:250]]
        plt.plot(year, y[0], year, y[1])
        plt.title("Populations Projections")
        plt.xlabel("Year")
        plt.legend(["france", "belgium"])
        plt.ylabel("Population")

        max_pop = max(max(y1), max(y2))
        yticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
        plt.yticks(yticks, ["{:,.0f}M".format(pop / 1e6) for pop in yticks])

        plt.show()

    except BaseException as e:
        print("MyError", e)


if __name__ == "__main__":
    main()

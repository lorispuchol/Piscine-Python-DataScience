from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def main():
    """Display graph of lifetime function of gpd for 1900 year"""
    try:
        fields = ["1900"]
        gdp_df = load(
            "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv",
            fields
        )
        lifetime_df = load("../life_expectancy_years.csv", fields)
        if gdp_df is None or lifetime_df is None:
            raise BaseException("A porbleme occured to load file")

        print(gdp_df)
        print(lifetime_df)

        x = np.array(gdp_df)
        y = np.array(lifetime_df)

        plt.plot(x, y, "ob")
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life expectancy")
        plt.xscale('log')
        plt.show()

    except BaseException as e:
        print("MyError", e)


if __name__ == "__main__":
    main()

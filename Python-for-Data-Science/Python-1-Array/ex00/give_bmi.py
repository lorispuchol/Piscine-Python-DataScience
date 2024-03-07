import numpy


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
) -> list[int | float]:

    """return a list of bmi calculated from of list of height and weight"""
    try:
        if len(height) != len(weight):
            raise BaseException("Height and weight have not the same lenght")
        if (
            (numpy.array(height).dtype != 'float64') and
            (numpy.array(height).dtype != 'int64')
        ):
            raise BaseException("Height is not a list of int or float")
        if (
            (numpy.array(weight).dtype != 'float64') and
            (numpy.array(weight).dtype != 'int64')
        ):
            raise BaseException("Weight is not a list of int or float")

        height_array = numpy.array(height)
        weight_array = numpy.array(weight)

        bmi = weight_array / (height_array * height_array)

    except BaseException as e:
        print("MyError:", e)
        return []
    return list(bmi)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """return True if bmi is above the limite"""
    return [x > limit for x in bmi]


def main():
    """Main de test"""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()

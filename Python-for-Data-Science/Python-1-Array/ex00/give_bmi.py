import numpy


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
) -> list[int | float]:
    """return a list of bmi calculated from of list of height and weight"""
    if len(height) != len(weight):
        return []
    height_array = numpy.array(height)
    weight_array = numpy.array(weight)

    bmi = weight_array / (height_array * height_array)
    return list(bmi)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """return True if bmi is above the limite"""
    return [x > limit for x in bmi]


def main():
    """Main de test"""
    height = [2.71, 1.15, 15]
    weight = [165.3, 38.4, 1000]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()

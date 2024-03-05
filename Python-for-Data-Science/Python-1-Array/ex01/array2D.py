import numpy as np


def slice_me(family: list, start: int, end: int) -> list:

    if not isinstance(family, list) or len(family) == 0:
        print("Error: Family is not a list or empty")
        return []
    sublist_lengths = {len(sublist) for sublist in family}
    if len(sublist_lengths) != 1:
        print("Error: All sublists in 'family' must have the same length")
        return []
    Arr = np.array(family)
    print("My shape is :", Arr.shape)
    truncated = Arr[start:end]
    print("My new shape is :", Arr.shape)
    return truncated

def main():
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

if __name__ == "__main__":
    main()
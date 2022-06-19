#Built-in imports
import sys

#External imports
import numpy as np

def calculate(numbers):
    if (len(numbers) != 9):
        raise ValueError("List must contain nine numbers.")

    data = np.array(numbers).reshape((3, 3))
    print(data.shape)

    keys = ["mean", "variance", "standard deviation", "max", "min", "sum"]

    operations = [np.mean, np.var, np.std, np.max, np.min, np.sum]

    values = []

    for oper in operations:
        values.append([
            oper(data, axis=0).tolist(),
            oper(data, axis=1).tolist(),
            oper(data)
        ])

    calculations = dict(zip(keys, values))

    return calculations

def main():
    test1 = [2,6,2,8,4,0,1,]
    print(calculate(test1))


if __name__ == "__main__":
    sys.exit(main())
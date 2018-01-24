import csv
import matplotlib.patches as mpatches
from matplotlib import pyplot as plt

def read_file():
    table_list = []
    with open('cars04.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if len(row) > 0:
                    table_list.append(row)
    return table_list



def main():
    table = read_file()
    print(table)
    counter = 0
    for cars in table:
        if counter > 0:

            try:
                x = float(cars[13])
            except:
                x = 0
            try:
                y = float(cars[14])
            except:
                y = 0

            try:
                size = (float(cars[16])*float(cars[16])) * 0.000004
            except:
                size = 0

            if cars[1] == "1":
                plt.scatter(x, y, c="#f46845", marker='s', s=size)
            elif cars[2] == "1":
                plt.scatter(x, y, c="g", marker='s', s=size)
            elif cars[3] == "1":
                plt.scatter(x, y, c="r", marker='s', s=size)
            elif cars[4] == "1":
                plt.scatter(x, y, c="c", marker='s', s=size)
            elif cars[5] == "1":
                plt.scatter(x, y, c="m", marker='s', s=size)
            elif cars[6] == "1":
                plt.scatter(x, y, c="y", marker='s', s=size)
            elif cars[7] == "1":
                plt.scatter(x, y, c="k", marker='s', s=size)
            elif cars[8] == "1":
                plt.scatter(x, y, c='#003182', marker='s')
        else:
            counter += 1

    plt.xlabel("HP")
    plt.ylabel("City MPG")
    plt.title("Scatterplot of horsepower versus city MPG")
    small = mpatches.Patch(color='#f46845', label='Small/Sporty/ Compact/Large Sedan')
    Sports = mpatches.Patch(color='g', label='Sports Car')
    SUV = mpatches.Patch(color='r', label='SUV')
    Wagon = mpatches.Patch(color='c', label='Wagon')
    Minivan = mpatches.Patch(color='m', label='Minivan')
    Pickup = mpatches.Patch(color='y', label='Pickup')
    AWD = mpatches.Patch(color='k', label='AWD')
    RWD = mpatches.Patch(color='#003182', label='RWD')
    plt.legend(handles=[small, Sports, SUV, Wagon, Minivan, Pickup, AWD, RWD])
    plt.show()



if __name__ == '__main__':
    main()

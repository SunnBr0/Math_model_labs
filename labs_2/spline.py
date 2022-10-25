import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

def inbuilt(x, y,xt):
    yi = 0
    temp = interpolate.splrep(x,y,s=0)
    yi = interpolate.splev(xt,temp,der=0)

    return yi

            

print("Введите количество графиков которые вы хотите увидеть(вводить цифры через пробел)\n")

array_coords = []

while 1:
    count_graphs = list(map(int, input("Образец написания: '1 2 3' - выведет 3 графика\n> ").split(' ')))

    for graph in count_graphs:
        match graph:
            case 1:
                file = open('1.txt','r')
                for coordinates in file:
                    array_coords.append(list(map(float, coordinates.split(' '))))
            case 2:
                file = open('2.txt','r')
                for coordinates in file:
                    array_coords.append(list(map(float, coordinates.split(' '))))
            case 3:
                file = open('3.txt','r')
                for coordinates in file:
                    array_coords.append(list(map(float, coordinates.split(' '))))
    

    for i in range(len(count_graphs)):
        x_array = array_coords[2*i]
        y_array = array_coords[2*i+1]
        sort_coord = sorted(zip(x_array,y_array))
        x_array = [x[0] for x in sort_coord]
        y_array = [x[1] for x in sort_coord]
        
        plt.scatter(x_array, y_array)
        

        on_x = float(input(f"Введите промежутное значение координаты 'x' графика: № {i+1}: от {min(x_array)} до {max(x_array)}\n> "))

        x1 = np.arange(x_array[0],x_array[-1],0.001)
        temp = interpolate.splrep(x_array,y_array,s=0)

        y1 = interpolate.splev(x1,temp,der=0)
        plt.plot(x1,y1)
        
        y = inbuilt(x_array, y_array, on_x)
        plt.scatter(on_x, y,color = 'black')
        print(f"Промежуточное значение 'y' графика: № {i+1}: ",y)


    plt.show()

    file.close()
    array_coords = []

    if input("Для завершения работы нажимте 'n'? (y/n)\n> ") == 'n':
            break
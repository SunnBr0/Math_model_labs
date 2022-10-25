import matplotlib.pyplot as plt
import numpy as np

def lagrange(x, y,xt):
    Ln_sum = 0
    for i in range(len(x)):
        li = 1
        for j in range(len(x)):
            if j != i:
                li*=(xt - x[j])/(x[i]-x[j])
        Ln_sum += li*y[i]
    return Ln_sum

            

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
        y1 = [lagrange(x_array, y_array, xi) for xi in x1]
        plt.plot(x1,y1)
        
        y = lagrange(x_array, y_array, on_x)
        plt.scatter(on_x, y,color = 'black')
        print(f"Промежуточное значение 'y' графика: № {i+1}: ",y)


    plt.show()

    file.close()
    array_coords = []

    if input("Для завершения работы нажимте 'n'? (y/n)\n> ") == 'n':
            break
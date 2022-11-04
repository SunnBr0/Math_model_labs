import matplotlib.pyplot as plt
import numpy as np

def gorner(n_pow_polinom,x,cof):
    p = cof[n_pow_polinom]
    for i in range(n_pow_polinom, 0, -1):
        p = p * x
        p = p + cof[i-1]
    return p

def sum_error_kvad(x,y,cof_polinom,n_pow_polinom):
    coef_list = list(cof_polinom)
    coef_list.reverse()
    sum = 0
  
    for i in range(len(x)):
        fx_gorner = gorner(n_pow_polinom, x[i], coef_list)
        sum += (y[i] - fx_gorner)**2
    print("Суммарная ошибка : ", sum)

def approximation(array_x, array_y,n_pow_polinom):
    #находит 
    cof_polinom = np.polyfit(array_x,array_y,n_pow_polinom)
    f = np.poly1d(cof_polinom)

    sum_error_kvad(array_x,array_y,cof_polinom,n_pow_polinom)

    x1 = np.arange(x_array[0],x_array[-1],0.001)
    y1 = f(x1)
    plt.plot(x1,y1)


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

        n_pow_polinom = int(input(f"Введите степень полинома графика: № {i+1}: больше {len(x_array)}\n> "))

        # x1 = np.arange(x_array[0],x_array[-1],0.001)
        # y1 = [approximation(x_array, y_array, xi) for xi in x1]
        # y1 = approximation(x_array, y_array, n_pow_polinom)
        approximation(x_array, y_array, n_pow_polinom)
        # plt.plot(x1,y1)
        


    plt.show()

    file.close()
    array_coords = []

    if input("Для завершения работы нажимте 'n'? (y/n)\n> ") == 'n':
            break
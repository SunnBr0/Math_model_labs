import matplotlib.pyplot as plt

def findY(array_x, array_y,xt):
    res = 0
    #Обработка ошибки если пользователь ввел значение "х" которое не принадлежит диапозону
    if(not(min(array_x)<=xt and xt<=max(array_x))):
        print("Ваше значение превосходит диапазон 'x'")
        raise ValueError("This is an ValueError")
    # пробегаемся по точкам графмика
    for j in range(len(array_x)):
                tempX = array_x[j]
                tempY = array_y[j]
                if(array_x[len(array_x)-1] == tempX):
                    break
                nextX = array_x[j+1]
                nextY = array_y[j+1]
                # ищем значение "y" при промежуточном "x",которое находится между двумя точками
                if tempX <= xt and xt <=nextX:
                    at = (nextY - tempY)/(nextX - tempX)
                    bt = tempY - at*tempX
                    res = xt*at+bt
                    return res


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
        plt.plot(x_array, y_array)

        on_x = float(input(f"Введите промежутное значение координаты 'x' графика: № {i+1}: от {min(x_array)} до {max(x_array)}\n> "))
        y = findY(x_array,y_array,on_x)
        plt.scatter(on_x, y,color = 'black')
        print(f"Промежуточное значение 'y' графика: № {i+1}: ",y)


    plt.show()

    file.close()
    array_coords = []

    if input("Для завершения работы нажимте 'n'? (y/n)\n> ") == 'n':
            break
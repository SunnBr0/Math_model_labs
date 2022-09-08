from warnings import catch_warnings
import matplotlib.pyplot as plt
import seaborn as sns

print("Введите количество графиков которые вы хотите увидеть(вводить цифры через пробел)\n")

array_coords = []

while 1:
    # кол-во графиков,которые вы хотите увидеть
    count_graphs = list(map(int, input("Образец написания: '1 2 3' - выведет 3 графика\n> ").split(' ')))

    # выбор метода отрисовки matplotlib или seaborn ()
    drawing_selection = input("С помощью чего вы хотите изобразить matplotlib или seaborn\nНапишите 'mtb' или 'sbrn':\n> ")

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
        if drawing_selection == "mtb":
            plt.scatter(array_coords[2*i], array_coords[2*i + 1])
        else:
            sns.lineplot(x = array_coords[2*i],y = array_coords[2*i + 1])

    plt.show()

    file.close()
    array_coords = []

    if input("Для завершения работы нажимте 'n'? (y/n)\n> ") == 'n':
            break
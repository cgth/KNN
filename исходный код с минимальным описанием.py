import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets

n_neighbors = 15 #K-целое значение, указанное пользователем. Количество соседей которое будет искаться

iris = datasets.load_iris() # выборка iris представляет из себя матрицу 150 строк на 4 столбца
X = iris.data[:, :2] #присваиваем X значения двух первых столбцов из выборки iris
y = iris.target #массив ответов, 150 цифр. ответ на каждую точку может быть один из трёх 0, 1, 2\

h = 0.02  # размер шага в сетке
# Создание цветовых карт
cmap_light = ListedColormap(['#bafffc', '#ffdede','#abffbd']) #цвета площадок
cmap_bold = ListedColormap(['Blue', 'Red', 'Lime']) #цвета точек

def knn(weights_): # параметр весовой функции можт принимать 2 значения 'uniform' или 'distance'
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights = weights_) # объявляю экземпляр класса
    clf.fit(X, y) # помещает в экземпляр класса данные

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1# находим минимальное и максимальное значение в первом столбце
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1# находим минимальное и максимальное значение во втором столбце

    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),  np.arange(y_min, y_max, h))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])    # Z хранит ответы для каждой точки на плоскости 3 цвета 3 разных значения
    Z = Z.reshape(xx.shape)

    plt.figure() #рисует 'uniform' . без этой строки рисует только 'distance'
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)#отрисовка цветов фона плоскости

    # Отрисовка по обучающей выборке
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor='black', s=20)#отрисовка точек на плоскости
        #edgecolor='black' цвет ободков вокруг точек.
    plt.title("3-Class classification (k = %i, weights = '%s')"% (n_neighbors, weights_ ))#отрисовка заголовка
    plt.show() #показать на экране рисунки


knn('uniform')#вклад в классификацию каждой точки одинаковый
knn('distance')#Используется весовая функция расстояния

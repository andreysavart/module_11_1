import requests

# Отправка GET-запроса
response = requests.get('https://jsonplaceholder.typicode.com/posts')
# Вывод данных в консоль
print(response.json())
27

import matplotlib.pyplot as plt

# Данные для графика
x = [1, 2, 3, 4, 7]
y = [2, 3, 7, 9, 15]

# Построение графика
plt.plot(x, y, marker='o')
plt.title('Пример линейного графика')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()

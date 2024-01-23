n = int(input())
max_values = []

for _ in range(n):
    # Считываем последовательность измерений
    sequence = input().split()
    
    # Преобразуем элементы последовательности в целые числа
    sequence = [int(x) for x in sequence]
    
    # Находим максимальное значение в последовательности
    max_value = max(sequence)
    
    # Добавляем максимальное значение в список
    max_values.append(max_value)

# Сортируем список максимальных значений по убыванию
max_values.sort(reverse=True)

# Выводим список максимальных значений, разделенных символом ";"
output = ";".join(str(x) for x in max_values)
print(output)
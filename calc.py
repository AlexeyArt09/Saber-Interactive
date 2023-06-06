# Калькулятор на Python

# Функция для вычисления математического выражения
def calculate(expression):
    try:
        result = eval(expression)  # Используем функцию eval() для вычисления выражения
        return result
    except Exception as e:
        return "Ошибка: " + str(e)

# Получение входного выражения от пользователя
expression = input("Введите математическое выражение: ")

# Вычисление и вывод результата
result = calculate(expression)
print("Результат:", result)

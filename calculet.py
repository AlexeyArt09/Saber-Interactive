def calculate(expression):
    try:
        result = eval(expression)  
        return result
    except Exception as e:
        return "Ошибка: " + str(e)
expression = input("Введите математическое выражение: ")
result = calculate(expression)
print("Результат:", result)

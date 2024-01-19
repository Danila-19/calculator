def calculator(input_string):
    try:
        elements = input_string.split()
        if len(elements) < 3:
            raise ValueError('т.к. строка не является'
                             'математической операцией')
        if len(elements) > 3:
            raise ValueError('Выражение слишком большое')
        a, operator, b = elements
        a, b = int(a), int(b)
        if a >= 11 and b >= 11:
            raise ValueError('Некорректный формат ввода')
        if a <= 0 or b <= 0:
            raise ValueError('Некорректный формат ввода')
        if operator not in ['+', '-', '*', '/']:
            raise ValueError('т.к. формат математической операции не'
                             'удовлетворяет заданию - два операнда и '
                             'один оператор (+, -, /, *)')
        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            result = a // b
        return result
    except ValueError as e:
        return f'Ошибка: {e}'


user_input = input('Введите выражение (например, 5 + 3): ')
result = calculator(user_input)
print(f'Результат: {result}')

def find_password(n):
    unique_pairs = []
    for i in range(1, 20):  # Перебираем все числа от 1 до 20 чтобы найти уникальные пары
        for j in range(i + 1, 20):  # Проверяем числа от i+1 чтобы не учитывать повторяющиеся пары
            if i + j == n:
                unique_pairs.append((i, j))

    # Формирование строки с парами для числа n
    password = ''.join([f"{pair[0]}{pair[1]}" for pair in unique_pairs])

    return password


n = 11  # Пример ввода числа
result = find_password(n)
print(f"Пароль для числа {n}: {result}")

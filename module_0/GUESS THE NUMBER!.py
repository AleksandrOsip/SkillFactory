def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того,
    больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1 # Счетчик попыток
    predict = np.random.randint(1,101) # Задали число
    while number != predict: # Задали цикл: если число не равно заданному...
        count+=1 # ...счетчик увеличивается на 1.
        if number > predict: # Если число больше заданного...
            predict += 1 # ...заданное число увеличиваем на 1.
        elif number < predict: # Если число меньше заданного...
            predict -= 1 # ...заданное число уменьшаем на 1.
    return(count) # выход из цикла, если угадали
print(f"Заданное число {predict}.")
print(f"Количество попыток {game_core_v2(number)}.")


def score_game(game_core_v1):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    return(score)

print(f"Ваш алгоритм угадывает число в среднем за {score_game(game_core_v1)} попыток")
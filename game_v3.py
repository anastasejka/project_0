import numpy as np
# Функция угадывания чисел с делением интервала пополам
def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    high = 101
    low = 1
    computer_number = np.random.randint(1, 101) # загадываем число
    predict = np.random.randint(low, high/2) #генерируем число,отправную точку для угадывания
    tries = 0 #счетчик попыток
    # цикл угадывания
    while computer_number != predict: 
        tries += 1
        if computer_number > predict:
            low = predict # Задаем нижнюю границу угадывания
            predict += (high-low)//2 # Продолжаем делить интервал угадывания наполовину
        elif computer_number < predict:
            high = predict # Задаем верхнюю границу угадывания
            predict -= (high-low)//2 # Продолжаем делить интервал угадывания наполовину
    return tries
print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)




























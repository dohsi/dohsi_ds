"""Игра угадай число
Комп сам угадывает рандомно
"""

from itertools import count
import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадывваем число 
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1

    Returns:
        int: число попыток
    """
    count = 0

    while True:
        count+=1
        predict_number = np.random.randint(1, 101) # предпологаемое число
        if number == predict_number:
            break # конец игры
    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем угадывает наш подход

    Args:
        random_predict ([type]): Функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за: {score}  попыток')
    return(score)

if __name__ == '__main__':
    # run
    score_game(random_predict)
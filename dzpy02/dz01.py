# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

coins = [0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0]
print(coins.count(0) if coins.count(0) < coins.count(1) else coins.count(1))

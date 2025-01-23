team1 = '"Мастера кода"'
team2 = '"Волшебники данных"'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = (score_1 + score_2)
time_total = float(format((team1_time + team2_time), '.2f'))
time_avg = format((time_total / tasks_total), '.2f')


def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
        result = f'Победа команды {team1}!'

    elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
        result = f"Победа команды {team2}"

    else:
        result = 'Ничья!'
    return result


# %s

print('В команде %s участников: %s!' % (team1, team1_num))
print('В команде %s участников: %s!' % (team2, team2_num))

print('Итого сегодня в командах участников: %s и %s \
и хотя это не честно, мы с напряжением будем следить \
за разворачивающимися событиями.' % (team1_num, team2_num))
print()

# Format

print('Количество решенных командой {0} задач: {1}!'.format(team2, score_2))
print('{1} сек. итоговое время которое потребовалось команде {0} \
для решения задач. '.format(team2,team2_time))
                              # Вероятно в задаче ошибка или ловушка т.к по условию команда т_2 а время ставится от т_1
print()

# f String

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result()}!')
print(f'Сегодня было решено {tasks_total} задач, \
в среднем по {time_avg} секунды на задачу!')
# Переменные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 350.4
challenge_result =()

# Определение результата соревнования
if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

print("Использование %")
team_members = "В команде Мастера кода участников: %d !" % team1_num
print(team_members)
team_members_2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(team_members_2)
print()
print("Использование .format()")
team2_score = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(team2_score)
team2_time = "Волшебники данных решили задачи за {:.1f} с !".format(team2_time)
print(team2_time)
print()
print("Использование f-строк")
teams_done = f"Команды решили {score_1} и {score_2} задач."
print(teams_done)
result_battle = f"Результат битвы: {challenge_result}"
print(result_battle)
tasks_time_total = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!"
print(tasks_time_total)

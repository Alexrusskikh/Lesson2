# Истоиическая викторина
# Укажите год рождения И.А.Крылова 1769
# Укажите год рождения П.И.Чайковского 1840
# Укажите год рождения Г.К.Жукова 1896
# Укажите год рождения Ю.А.Гагарина 1934
# Укажите год рождения В.И.Ленина 1870
# правильные ответы
rightSumBall = 0
# неверные ответы
wrongSumBall = 0
NewRound = "Да"
while NewRound == "Да":
    # Вопрос1
    test = input("Укажите год рождения И.А.Крылова '1769': ")
    if test == '1769':
        print("Верно!!!!")
        rightSumBall = rightSumBall + 1
    else:
        print("Не верно!!!!")
        wrongSumBall = wrongSumBall + 1
    # Вопрос2
    test = input("Укажите год рождения П.И.Чайковского '1840': ")
    if test == "1840":
        print("Верно!!!!")
        rightSumBall = rightSumBall + 1
    else:
        print("Не верно!!!!")
        wrongSumBall = wrongSumBall + 1
    # Вопрос3
    test = input("Укажите год рождения Г.К.Жукова '1896': ")
    if test == "1896":
        print("Верно!!!!")
        rightSumBall = rightSumBall + 1
    else:
        print("Не верно!!!!")
        wrongSumBall = wrongSumBall + 1
    # Вопрос4
    test = input("Укажите год рождения Ю.А.Гагарина '1934': ")
    if test == "1934":
        print("Верно!!!!")
        rightSumBall = rightSumBall + 1
    else:
        print("Не верно!!!!")
        wrongSumBall = wrongSumBall + 1
    # Вопрос5
    test = input("Укажите год рождения В.И.Ленина '1870': ")
    if test == "1870":
        print("Верно!!!!")
        rightSumBall = rightSumBall + 1
    else:
        print("Не верно!!!!")
        wrongSumBall = wrongSumBall + 1
    percentRight = (rightSumBall * 100) / 5
    percentWrong = (wrongSumBall * 100) / 5
    print(f'Правильных ответов -  {rightSumBall},  это {percentRight} %')
    print(f'Неверных ответов -  {wrongSumBall}, это {percentWrong} %')
    NewRound = input("Хотите начать сначала? (Да-Нет): ")
print("Викторина завершена")

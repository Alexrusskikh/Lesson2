# указать год рождения А.С.Пушкина
BornYearPushkin = input("Укажите год рождения А.С Пушкина: ")
if BornYearPushkin == "1799":
    print("Верно! Эрудит!")
    BornDayPushkin = input("Укажите дату рождения А.С Пушкина, например - '6 июня': " )
    if BornDayPushkin == '6 июня':
        print("Верно! Умница!")
    else:
        print("Уточните в первоисточниках....., не отчаивайтесь")
else:
    print("Уточните в первоисточниках....., не отчаивайтесь")
print ("Тест  закончен")
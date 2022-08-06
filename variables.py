# описание пациента
# импорт класса из модуля
from datetime import datetime
# текущая дата
today = datetime.today()
print('Сегодня: ', today.strftime("%d.%m.%Y"))
# дата рождения
dateОfBirth = input("Введите дату рождения (dd.mm.yyyy):\n")
birthdate = datetime.strptime(dateОfBirth, "%d.%m.%Y")
age = int((today - birthdate).days / (365))
print("Возраст пациента:", age, "год(а)")

# фамилия, строкавая str
surname = input('Введите фамилию: ')
# имя, строкавая str
name = input('Введите имя: ')

# отчество, строкавая str
patronymic = input('Введите отчество: ')
# тип населенного пункта проживания,  лучше из списка или  словаря сделать
locality = input('Введите тип населенного пункта: ')

# улица
street = input('Введите улицу: ')

# трудоустройство bool  - логический тип (Истина или ложь)
employment_stan = "Да"
employment = input("Пациент  трудоустроен(Да-нет): ")
comparison_emp = employment == employment_stan
if comparison_emp == True:
    print("Клиент трудоустроен, нуждается в оформлении ЛВН")
else:
    print("Так держать, не че горбатиться на дядю....")
print("Трудоустройство: ", comparison_emp)


# пенсионер bool  - логический тип (Истина или ложь)
retiree_stan = "Да"
retiree = input("Пенсионер (Да-нет): ")
comparison_ret = retiree == retiree_stan
if comparison_ret == True:
    print("Пенсионер, но если работает нужен ЛВН")
else:
    print("Много нас таких...")
print("Пенсионер: ", comparison_ret)


# обратился впервые bool  - логический тип (Истина или ложь)
primary_stan = "Да"
primary = input("Первичное обращение (Да-нет): ")
comparison_prim = primary == primary_stan
if comparison_prim == True:
    print("Все бывает впервые....")
else:
    print("Много нас таких...")
print("Первичное обращение: ", comparison_prim)


# float - цисло с плавающей точкой
temperature = float(input("Укажите температуру тела: "))
print("Температура тела:", temperature)

print("today:", type(today), "surname:", type(surname), "name:", type(name), "patronymic:\n",
      type(patronymic), "dateОfBirth:", type(dateОfBirth), "age:", type(age), "locality\n:", type(locality),
      "Street :", type(street), "employment", type(comparison_emp), "retiree:", type(comparison_ret), "primary:\n", type(comparison_prim),
      "temperature :", type(temperature))
print("End")
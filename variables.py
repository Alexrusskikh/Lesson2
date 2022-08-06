# описание пациента
# импорт класса из модуля
from datetime import datetime
# текущая дата
today = datetime.today()
print(type(today))
print('Сегодня: ', today.strftime("%d.%m.%Y"))
# дата рождения
dateОfBirth = input("Введите дату рождения (dd.mm.yyyy):\n")
birthdate = datetime.strptime(dateОfBirth,"%d.%m.%Y")
age= int((today- birthdate).days / (365))
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
if employment == employment_stan:
            print("Клиент трудоустроен, нуждается в оформлении ЛВН")
else:
      print("Так держать, не че горбатиться на дядю....")
print(employment == employment_stan)
# пенсионер bool  - логический тип (Истина или ложь)
retiree_stan = "Да"
retiree = input("Пенсионер (Да-нет): ")
if retiree == retiree_stan:
            print("Пенсионер, но если работает нужен ЛВН")
else:
      print("Много нас таких...")
print(retiree == retiree_stan)
# обратился впервые bool  - логический тип (Истина или ложь)
primary_stan = "Да"
primary = input("Первичное обращение (Да-нет): ")
if primary == primary_stan:
            print("Все бывает впервые....")
else:
      print("Много нас таких...")
print(retiree == retiree_stan)
#float - цисло с плавающей точкой
temperature = 36.6
print("today:", type(today), "surname:", type(surname), "name:", type(name), "patronymic:\n",
      type(patronymic), "dateОfBirth:", type(dateОfBirth), "age:", type(age), "locality\n:", type(locality),
      "Street :", type(street), "employment", type(employment), "retiree:", type(retiree), "primary:\n", type(primary),
      "temperature :", type(temperature))
print("End")

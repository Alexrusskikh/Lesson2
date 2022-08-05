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
Street = input('Введите улицу: ')
# трудоустройство bool  - логический тип (Истина или ложь)
employment = input("Пациент  трудоустроен(Да-нет): ")
if employment == "Да":
            print("Клиент трудоустроен, нуждается в оформлении ЛВН")
else:
      print("Так держать, не че горбатиться на дядю....")
# пенсионер bool  - логический тип (Истина или ложь)
retiree = input("Пенсионер (Да-нет): ")
if retiree == "Да":
            print("Пенсионер, но если работает нужен ЛВН")
else:
      print("Много нас таких...")
# обратился впервые bool  - логический тип (Истина или ложь)
primary = input("Первичное обращение (Да-нет): ")
if primary == "Да":
            print("Все бывает впервые....")
else:
      print("Много нас таких...")
#float - цисло с плавающей точкой
temperature = 36.6
print("today:", type(today), "surname:", type(surname), "name:", type(name), "patronymic:\n",
      type(patronymic), "dateОfBirth:", type(dateОfBirth), "age:", type(age), "locality\n:", type(locality),
      "Street :", type(Street), "employment", type(employment), "retiree:", type(retiree), "primary:\n", type(primary),
      "temperature :", type(temperature))
print("End")

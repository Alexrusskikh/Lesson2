# описание пациента
# импорт класса из модуля
from datetime import date
# текущая дата
today = date.today()
print('Сегодня: ', today.strftime("%d.%m.%Y"))
# фамилия, строкавая str
surname = input('Введите фамилию: ')
# имя, строкавая str
name = input('Введите имя: ')
# отчество, строкавая str
patronymic = input('Введите отчество: ')
# дата рождения
dateОfBirth = input("Введите дату рождения (dd.mm.yyyy):\n")
# возраст, надо  сделать расчет,  пока не понял как
age = int(input('Введите возраст:'))
# тип населенного пункта проживания,  лучше из списка или  словаря сделать
locality = input('Введите тип населенного пункта: ')
# улица
Street = input('Введите улицу: ')
# трудоустройство bool  - логический тип (Истина или ложь)
employment = True
# пенсионер bool  - логический тип (Истина или ложь)
retiree = True
# обратился впервые bool  - логический тип (Истина или ложь)
primary = True
#float - цисло с плавающей точкой
temperature = 36.6
print("today:", type(today), "surname:", type(surname), "name:", type(name), "patronymic:\n",
      type(patronymic), "dateОfBirth:", type(dateОfBirth), "age:", type(age), "locality\n:", type(locality),
      "Street :", type(Street), "employment", type(employment), "retiree:", type(retiree), "primary:\n", type(primary),
      "temperature :", type(temperature))
print("End")

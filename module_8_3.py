class Car:
    def __init__(self,model,__vin,number):
        self.model = model
        if self.__is_valid_vin(__vin):
           self.__vin=__vin
        if self.__is_valid_numbers(number):
           self.number = number
    def __is_valid_vin(self,vin_number):
        if not isinstance(vin_number,int):
            raise IncorrectVinNumber('Некоректный тип vin номера ')
        if not  (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber ('некоректный диапазон для vin омера')
        return True
    def __is_valid_numbers(self,number):
        if not isinstance(number,str):
            raise IncorrectCarNumbers ('Некорректный тип данных для номеров')
        if  len(number) != 6 :
            raise IncorrectCarNumbers ('Неверная длина номера')
        return True
class IncorrectVinNumber (Exception):
    def __init__(self,message):
        self.message=message
class IncorrectCarNumbers (Exception):
    def __init__(self,message):
        self.message=message


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')




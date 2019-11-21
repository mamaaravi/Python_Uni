# Визначивши клас із завдання 6 за базовий, сформувати похідні класи.
# Перевизначити методи базового класу та описати нові методи згідно з варіантом завдання.
# Створити масив з об’єктів базового і похідного класів. Показати роботу усіх методів.

# 12. Похідні класи “Квиток міжнародного сполучення” (поле: прізвище)
# та “Квиток місцевого призначення” (поле: наявність пільги).
# Обчислення вартості квитка міжнародного сполучення проводити
# з урахуванням кілометражу та наданням знижки за попереднє бронювання.
# Вартість квитка місцевого призначення обчислюють з урахуванням наявних пільг пасажира
# (наприклад, дитячий – 50 %, пенсійний – 30 %, інваліди 1 групи – безкоштовно).

from classTicket import Ticket

class InternationalTicket(Ticket):
    def __init__(self, arrival_station, time_of_departure_and_arrival, place_number, name, surname, reservation, kilometrage):
        super().__init__(arrival_station, time_of_departure_and_arrival, place_number)
        self.name = name
        self.surname = surname
        self.reservation = reservation
        self.kilometrage = kilometrage
    def price_of_ticket(self):
        kForKilometrage = 0.05                  # з урахуванням кілометражу
        discount = 0.3                          # наданням знижки за попереднє бронювання
        return  (super().price_of_ticket() + self.kilometrage*kForKilometrage) -  (super().price_of_ticket() + self.kilometrage*kForKilometrage)*discount if self.reservation=='True' else (super().price_of_ticket() + self.kilometrage*kForKilometrage)


listOfTickets = list()
with open('datasForIntenationalTicket.txt') as tickets:
    for line in tickets:
        listOfTickets.append(InternationalTicket(line.split(' ')[0], line.split(' ')[1], line.split(' ')[2], line.split(' ')[3], line.split(' ')[4], line.split(' ')[5], float(line.split(' ')[6])))
for item in listOfTickets:
    print('______________')
    item.ticket_info()

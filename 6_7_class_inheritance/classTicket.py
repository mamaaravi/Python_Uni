# Описати клас на основі заданої предметної області.
# Створити масив об’єктів класу (інформацію вводити з файлу),
# та за допомогою створеного меню продемонструвати результати виконання методів для кожного елемента масиву.

# 12. Клас “Квиток”.
# Поля:
# • станція прибуття;
# • час прибуття та відправлення;
# • номер місця;
# Завдання №6. Класи (4б).
# • вартість.
# Методи:
# • перетворення стрічки зі заданими часом прибуття і відправлення в числовий тип і обчислення часу поїздки у хвилинах;
# • обчислення вартості квитка (згідно з нормою за одиницю часу тривалості поїздки).

class Ticket:
    def __init__(self, arrival_station, time_of_departure_and_arrival, place_number):
        self.arrival_station = arrival_station
        self.time_of_departure_and_arrival = time_of_departure_and_arrival
        self.place_number = place_number

    def ticket_info(self):
        print("Arrival station:", self.arrival_station)
        print("Time of departure:", self.time_of_departure_and_arrival.split('-')[0])
        print("Time of arrival:", self.time_of_departure_and_arrival.split('-')[1])
        print("Number of a place:", self.place_number)
        print("Price:", self.price_of_ticket())

    def duration_of_journey(self):
        tempSplit = self.time_of_departure_and_arrival.split('-')
        duration = abs(int(tempSplit[0].split(':')[0]) * 60 + int(tempSplit[0].split(':')[1]) - int(
            tempSplit[1].split(':')[0]) * 60 - int(tempSplit[1].split(':')[1]))
        if (duration > 720):
            duration -= 1440
        return abs(duration)

    def price_of_ticket(self):
        return self.duration_of_journey() / 60 * 3



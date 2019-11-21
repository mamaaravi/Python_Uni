# Вартість квитка місцевого призначення обчислюють з урахуванням наявних пільг пасажира
# (наприклад, дитячий – 50 %, пенсійний – 30 %, інваліди 1 групи – безкоштовно).


from classTicket import Ticket

class LocalTicket(Ticket):
    def __init__(self, arrival_station, time_of_departure_and_arrival, place_number, privilege):
        super().__init__(arrival_station, time_of_departure_and_arrival, place_number)
        self.privilege = privilege
        self.discount = 0
    def price_of_ticket(self):

        if self.privilege == 'Aged\n':

            self.discount = 0.3
        if self.privilege == 'Child\n':

            self.discount = 0.5
        if self.privilege == 'InvalidFirstGroup\n':

            self.discount = 1
        print(self.privilege)
        return  super().price_of_ticket() -  super().price_of_ticket() * self.discount


listOfTickets = list()
with open('datasForLocalTicket.txt') as tickets:
    for line in tickets:
        listOfTickets.append(LocalTicket(line.split(' ')[0], line.split(' ')[1], line.split(' ')[2], line.split(' ')[3]))
for item in listOfTickets:
    print('______________')
    item.ticket_info()

#OUTPUT SAMPLE:
# ______________
# Arrival station: Lviv
# Time of departure: 23:45
# Time of arrival: 01:45
# Number of a place: 1
# Child

# Price: 3.0
# ______________
# Arrival station: Lviv
# Time of departure: 23:45
# Time of arrival: 01:45
# Number of a place: 2
# Aged

# Price: 4.2
# ______________
# Arrival station: Kyiv
# Time of departure: 18:45
# Time of arrival: 23:56
# Number of a place: 3
# InvalidFirstGroup

# Price: 0.0
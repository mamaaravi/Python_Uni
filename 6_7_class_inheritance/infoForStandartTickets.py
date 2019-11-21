from classTicket import Ticket

listOfTickets = list()

with open('datasForStandartTicket.txt') as tickets:
    for line in tickets:
        listOfTickets.append(Ticket(line.split(' ')[0], line.split(' ')[1], line.split(' ')[2]))

for item in listOfTickets:
    item.ticket_info()


# OUTPUT SAMPLE:

# Arrival station: Lviv
# Time of departure: 23:45
# Time of arrival: 01:45
# Number of a place: 1

# Price: 6.0
# Arrival station: Lviv
# Time of departure: 23:45
# Time of arrival: 01:45
# Number of a place: 2

# Price: 6.0
# Arrival station: Kyiv
# Time of departure: 18:45
# Time of arrival: 23:56
# Number of a place: 3
# Price: 15.55
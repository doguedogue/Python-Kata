from datetime import timedelta, datetime

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f'{destination} Arrival: %A %H:%M')


def distance_from_earth(destination):
    if destination == 'Moon':
        return '238,855'
    else:
        return 'Unable to compute to that destination'


def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24        


def variable_length(*args):
    print(args)


def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f'Total time to launch is {total_minutes} minutes'
    else:
        return f'Total time to launch is {round(total_minutes/60,2)} hours'
    

def variable_length_key_word(**kwargs):
    print(kwargs)


def crew_members(**kwargs):
    print(f'{len(kwargs)} astronauts assigned for this mission:')
    for title, name in kwargs.items():
        print(f'{title}: {name}')


def main():
    print(distance_from_earth('Moon'))
    print(round(days_to_complete(238855, 75)))
    print(arrival_time('Moon'))
    print(arrival_time('Moon',hours=0))
    print(arrival_time('Orbit', hours=0.13))
    variable_length()
    variable_length(None)
    variable_length('param1', 'param2', 3, 4.5, True)
    print (sequence_time(4, 14, 18))
    print (sequence_time(55, 66, 118))
    variable_length_key_word()
    variable_length_key_word(tanks=1, day='Wednesday', pilots=3)
    crew_members(captain='Neil Armstrong', pilot='Buzz Aldrin', command_pilot='Michael Collins', flight_engineer='Rodolfo Neri Vela')


if __name__ == '__main__':
    main()
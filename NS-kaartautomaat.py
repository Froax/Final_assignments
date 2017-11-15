def inlezen_beginstation(stations):
    beginstation = ''
    while True:
        user = input('Wat is je beginstation?: ')
        if user in stations:
            beginstation = user
            print('U heeft gekozen voor {0}'.format(user))
            break
        print("Deze trein komt niet in {0}".format(user))
    return beginstation

def inlezen_eindstation(stations, beginstation):
    eindstation = ''
    while True:
        user = input('Wat is je eindstation?: ')
        if user in stations:
            if stations.index(user) < stations.index(beginstation):
                print("Deze trein komt niet in {0}".format(user))
            else:
                eindstation = user
                print('U heeft gekozen voor {0}'.format(user))
                break
        print("Deze trein komt niet in {0}".format(user))
    return eindstation

def omroepen_reis(stations, beginstation, eindstation):
    begint = stations.index(beginstation)
    eindst = stations.index(eindstation)
    print('Het beginstation {0} is het {1}e station in het traject.'.format(beginstation, begint))
    print('Het eindstation {0} is het {1}e station in het traject.'.format(eindstation, eindst))

    print('Afstand: ' + str((eindst - begint)) + ' stations')
    print('Kosten: ' + str(5 * (eindst - begint)) + ' euro')
    print('Je stapt in bij {0}'.format(beginstation))
    for i in range(begint + 1, eindst - 1):
        print('-', stations[i])
    print('Je stapt uit bij {0}'.format(eindstation))


stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)

def standaardprijs(afstandKM):
    if afstandKM > 50:
        return 15 + (afstandKM - 50) * 0.6
    elif afstandKM <= 0:
        return 0
    else:
        return afstandKM * 0.8


def ritprijs(leeftijd, weekendrit, afstandKM):
    standaard = standaardprijs(afstandKM)
    prijs = 0
    if leeftijd <= 12 or leeftijd >= 65:
        if weekendrit:
            prijs = standaard * 0.65
        else:
            prijs = standaard * 0.7
    elif weekendrit:
        prijs = standaard * 0.6
    return prijs

print(ritprijs(12, False, 10))
print(ritprijs(12, False, 60))
print(ritprijs(12, False, 100))
print(ritprijs(12, False, -1))
print(ritprijs(12, True, 10))
print(ritprijs(12, True, 60))
print(ritprijs(12, True, 100))
print(ritprijs(12, True, -1))
print(ritprijs(11, False, 10))
print(ritprijs(11, False, 60))
print(ritprijs(11, False, 100))
print(ritprijs(11, False, -1))
print(ritprijs(11, True, 10))
print(ritprijs(11, True, 60))
print(ritprijs(11, True, 100))
print(ritprijs(11, True, -1))
print(ritprijs(64, False, 10))
print(ritprijs(64, False, 60))
print(ritprijs(64, False, 100))
print(ritprijs(64, False, -1))
print(ritprijs(64, True, 10))
print(ritprijs(64, True, 60))
print(ritprijs(64, True, 100))
print(ritprijs(64, True, -1))
print(ritprijs(65, False, 10))
print(ritprijs(65, False, 60))
print(ritprijs(65, False, 100))
print(ritprijs(65, False, -1))
print(ritprijs(65, True, 10))
print(ritprijs(65, True, 60))
print(ritprijs(65, True, 100))
print(ritprijs(65, True, -1))

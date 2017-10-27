def standaardprijs(afstandKM):
    afstandKM = input('Hoeveel kilometer wilt u gaan reizen:')
    if afstandKM<=50:
        standaardprijs=int(afstandKM)*0.80
    else:
        verder_dan_50=int(afstandKM)-50
        standaardprijs=15+(verder_dan_50*0.60)
    return standaardprijs

leeftijd=0
weekendrit = input('Welke dag gaat u reizen:')
def ritprijs(leeftijd, weekendrit):
    if weekendrit=='zondag' or 'zaterdag':
        weekendrit=True
    else:
        weekendrit=False
    leeftijd = input('Wat is u leeftijd:')
    if leeftijd<15 and leeftijd>65 and str(weekendrit)==False:
        ritprijs=standaardprijs*0.30
        return ritprijs
    elif leeftijd<15 and leeftijd>65 and weekendrit==True:
        ritprijs=standaardprijs*0.35
        return ritprijs
    if  leeftijd>15 and leeftijd<65 and weekendrit==True:
        ritprijs=standaardprijs*0.40
        return ritprijs
    else:
        ritprijs=standaardprijs
        return ritprijs
    print('is ritprijs bedraagd {} euro'.format(str(ritprijs)))
print(ritprijs(weekendrit, leeftijd))


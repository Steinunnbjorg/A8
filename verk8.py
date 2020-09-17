# Ætlum að gera leik sem snýst um að komast á milli ákveðna hólfa og til að komast þar á milli segir maður hvort maður vilji fara norður/
# suður, austur eða vestur.

# Til þess að gera þetta forrit þá búum við til 2 föll og síðan eina while lykkju sem bindur föllin saman

def change_location(direction,position,allowed):                # Fall eitt, notað til að staðsetja hnitin, þar sem þau eru sett upp sem xy
    direction = direction.upper()
    if direction== 'N' and allowed.find("N") != -1:
        position += 1
    elif direction== 'E' and allowed.find("E") != -1:
        position += 10
    elif direction== 'S' and allowed.find("S") != -1:
        position -= 1
    elif direction== 'W' and allowed.find("W") != -1:
        position -= 10
    else:
        print("Not a valid direction!")                         # ef ofantalið er ekki uppfyllt er þetta prentað
    return position

def change_allowed(position):                           # Fall tvö sem segir hvert er hægt að fara/hvað leiðir eru opnar
    if (position ==11) or (position ==21):
        return 'N'
    elif position==32:
        return 'NS'
    elif position==12:
        return 'NSE'
    elif position==22:
        return 'SW'
    elif position==13:
        return 'ES'
    elif position==23:
        return 'EW'
    elif position ==33:
        return 'SW'

position=11             # skilgreina upphafsstaðsetningu
N = '(N)orth'
S = '(S)outh'
W = '(W)est'
E = '(E)ast'
text= 'You can travel: '    # þessi texti kemur í öllum print skipunum, svo það er betra að hafa hann hér

while position!=31:
    if (position == 11) or (position == 21):
        print("{}{}.".format(text,N))
    elif position == 12:
        print("{}{} or {} or {}.".format(text,N,E,S))
    elif position == 13:
        print("{} {} or {}.".format(text,E,S))
    elif position == 22:
        print("{}{} or {}.".format(text,S,W))
    elif position == 23:
        print("{}{} or {}.".format(text,E,W))
    elif position == 32:
        print("{}{} or {}.".format(text,N,S))
    elif position == 33:
        print("{}{} or {}.".format(text,S,W))
    direction = input("Direction: ")
    position = change_location(direction,position,change_allowed(position)) 

print("Victory!")
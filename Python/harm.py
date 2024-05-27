from Class import Xxxxxxxxxxxxx

with open('xxxxxxxxxxxxxxx.csv', 'r', encoding='utf-8') as f:
    myList = [Xxxxxxxxxxxxx(sor) for sor in f]

print(f'A listában lévő elemek száma: {len(myList)}')

legnagyobb_elem = max(myList, key=lambda x: x.xxxxxxxxxxxx) # x. után az kell, amire szeretnél max-ot keresni pl: x.ar

legkisebb_elem = min(myList, key=lambda x: x.xxxxxxxxxxxx) # x. után az kell, amire szeretnél min-t keresni pl: x.ar

xxxxxxxxx_elemek_osszeadasa = sum(i.xxxxxxxxxxxx for i in myList if xxxxxxxxxxx) # xxxxxxxxxxx helyére feltételt kell írni 
# Ha nincs feltétel akkor töröld ki: if xxxxxxxxxxxxx


xxxxxxxx_felteteles_kereses_count = 0

for i in myList:
    if xxxxxxxxxxx: # xxxxxxxxxxx helyére feltétel
        xxxxxxxx_felteteles_kereses_count += 1

myDict = {}
for i in myList:
    myDict[i.xxxxxxxxxxxx] = myDict.get(i.xxxxxxxxxxxx, 0) + 1 
# xxxxxxxxxxxx helyére a classnak kell a tulajdonsága.
# a get fogja a i.xxxxxxxxxxxx értéket, hozzáad 1-et, ha nincs akkor 0
# + 1 helyett lehet más is

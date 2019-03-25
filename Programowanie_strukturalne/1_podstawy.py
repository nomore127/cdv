print("CDV")
print(2)

#potęga
potega = 2 ** 10
print(potega)

tekst = "cdv"
print(tekst * 2)

#pobieranie danych z klawiatury
imie = input()
print("Twoje imię podane z klawiatury: " + imie)

nazwisko = input()
print("Twoje imię: " + imie + ", Twoje nazwisko: " + nazwisko)

dlugosc = len(nazwisko)
print (dlugosc)

print(type(nazwisko)) #string
print(type(dlugosc)) #intiger
print("Długość nazwiska: ", dlugosc)
dlugosc = str(dlugosc) #konwersja typu danych na int/str
print("Długość nazwiska: " + dlugosc)

#Użytkownik wpisuje z klawiatury swój wiek
#wyswietl dane w formacie: Twój wiek: ... lat
print("Podaj swój wiek: ", end="")
wiek = input()
print("Twój wiek: ", wiek, "lat")


Nazwisko = "Kowalski"
pierwszyZnak = Nazwisko[0]
print(pierwszyZnak)
ostatniZnak = Nazwisko[len(Nazwisko) - 1]
print(ostatniZnak)
ostatniZnak = Nazwisko[- 1]
print(ostatniZnak)

#konwersja
x = "5"
print(type(x)) #str
x = int(x)
print(type(x)) #int

y = 4
print(type(y)) #int
y = y/2
print(type(y)) #float

wiekk = 21
print("Twój wiek:", wiekk)
wiekk = str(wiekk)
print("Twój wiek: " + wiekk)

Nazwisko = "Kowalski"
print(Nazwisko[0]) #K
print(Nazwisko[0:3]) #Kow
print(Nazwisko[-2]) #k
print(Nazwisko[-2:]) #ki
print(Nazwisko[:-2]) #Kowalsk
print(Nazwisko[:-2:2]) #ko


print()

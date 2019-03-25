tekst = "Anna, paweł, TomEK"

tab = tekst.split(", ")
print(tekst)
print(tab)

imie1 = tab[0]
print(imie1) # Anna
print(type(tab)) #list

print("Twoje imię: " + imie1)
imieDuze = imie1.upper()
print(imieDuze)
imieMale = imie1.lower()
print(imieMale)

#sprawdzenie zawartosci
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc)
print(type(zawartosc)) #bool

nazwisko = ""
zawartosc = nazwisko.isalpha()
print(zawartosc)
print(type(zawartosc)) #false

imie = "Julia"
print("\nDane użytkownika\nMasz na imię: ", imie)

text1 = "Jan\n"
text2 = "Nowak"
print(text1 + text2)

text1 + text1.rstrip()
print(text1 + text2)
print(text1 + " " + text2)

#wyświetlanie łańcuchów znaków

#wszystkie wersje Pythona
text = "%s, Java i %s" % ("PHP","Python")
print(text)

#Najnowsze wersje Pythona >2.6
text ="{1}, Java i {0}".format("PHP","Python")
print(text)

#help(text.replace)
new = text.replace("PHP","C#")
print(new)


#wypisanie danych
rok = 2019
miesiac = "marzec"
dzien = 25

print("Data: ",end="")
print(dzien,miesiac,rok)

print("Data: ",end="")
print(dzien,miesiac,rok,sep="-")








print()

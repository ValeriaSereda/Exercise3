# zadanie 1.1

hello = "Hello"
student = "Ola"

"hello {}".format("student")
print(hello, student)

# zadanie 1.2
print ('Wpisz swoje imie:')

student = input()

print ('Hello' " " + student)

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]

liczba_studentow = len(studenci)
print('Liczba studentow wynosi:' + str(liczba_studentow))

# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

for i in studenci:
    print('Hello'" " + i)

# zadanie 1.5

liczba = 3
potega = 4

wynik = liczba ** potega

print('Wynik wynosi:' + str(wynik))

# zadanie 1.6

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count('(')

print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

# zadanie 1.7

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci_sort = sorted(studenci, key=lambda x: x.split()[0])
for student in studenci_sort:
    print(student)

# zadanie 1.8

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

# oczekiwany rezultat:
# Barbara Kowalska
# Jan Niezbedny
# Tomasz Nijaki
# Anna Szczesny
studenci_sort = sorted(studenci, key=lambda x: x.split()[1])
for student in studenci_sort:
    print(student)
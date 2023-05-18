# zadanie 1.1

hello = "Hello"
student = "Ola"


"hello {}".format("student")
print(hello, student)

# zadanie 1.2
print ('Wpisz swoje imie:')

student = input()

print ('Hello' " " + student)

# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

liczba_studentow = len(studenci)
print('Liczba studentów wynosi:' + str(liczba_studentow))

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

# posortuj alfabetycznie (od imienia) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci_sort = sorted(studenci, key=lambda x: x.split()[0])
for student in studenci_sort:
    print(student)

# zadanie 1.8

# posortuj alfabetycznie (od imienia) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci_sort = sorted(studenci, key=lambda x: x.split()[1])
for student in studenci_sort:
    print(student)

# zadanie 1.9

# policz wszystkich studentow z tablicy, ktorych nazwisko zaczyna sie na N
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
liczba_n = 0
for i in studenci:
    nazw = i.split()[1]
    if nazw.startswith('N'):
        liczba_n = liczba_n + 1

print('Liczba studentow na N wynosi:' + str(liczba_n))

# zadanie 1.10

def czy_istnieje_funkcja_liniowa(wykres):
    x = [punkt[0] for punkt in wykres] 
    y = [punkt[1] for punkt in wykres]  

    if len(set(x)) == 1:
        return True 

    n = len(wykres)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x[i] * y[i] for i in range(n))
    sum_x2 = sum(x[i] ** 2 for i in range(n))

    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    b = (sum_y - a * sum_x) / n
    for i in range(n):
        if y[i] == a * x[i] + b:
            return True
    return False

wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

wykres_1_funkcja_liniowa = czy_istnieje_funkcja_liniowa(wykres_1)
wykres_2_funkcja_liniowa = czy_istnieje_funkcja_liniowa(wykres_2)
wykres_3_funkcja_liniowa = czy_istnieje_funkcja_liniowa(wykres_3)

if wykres_1_funkcja_liniowa:
    print("Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_1 nie mozna wyznaczyc funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_2 nie mozna wyznaczyc funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktow w wykres_3 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.")

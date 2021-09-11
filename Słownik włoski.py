import json
from operator import itemgetter
from itertools import groupby

m = "*"
print(80 * m)
print(35 * " ", "Instrukcja", 40 * " ")
print(80 * m)
print("Witaj w prostym słowniku, w którym możesz zapisywać i wywoływać pojedyncze słowa")
print(80 * "-")

rzeczowniki = {}

while(True):
    
    print("\n1: Dodaj słowo *")
    print("2: Wyszukaj słowo*")
    print("3: Usuń słowo *")
    print("4: Pokaż zapisane słowa alfabetycznie *")
    print("5: Zamknij program *")
    choice = (input("\nWybierz: "))

    if choice == "1":
        new = input("\Jakie słowo w języku polskim chcesz dodać?: ")
        it_word = input("\nJakie jest jego tłumaczenie na język włoski?: ")
        rzeczowniki[new] = it_word
#         rzeczowniki[next_word] = new
        with open('slownik.txt', 'a', encoding='utf-8') as plik:
            plik.write(json.dumps(rzeczowniki))
        plik.close()
        print("Dodano")
       
    elif choice == "2":
        word = input("Czego szukasz?: ")
        if word in rzeczowniki:
            print(rzeczowniki)
            continue
        if word not in rzeczowniki:
            print("Nie znaleziono")
            continue
          
    elif choice == "3":
        word = input("Podaj slowo: ")
        if word in rzeczowniki:
            del rzeczowniki[word]

    elif choice == "4":
            with open("slownik.txt", "r") as plik:
                data = (json.load(plik))
                print(data)
        
    elif choice != "1" "2" "3":
        print("Postepuj wg instrukcji ")
        continue
    
    else:
        choice == "5"
        print("Program has ended")
        break

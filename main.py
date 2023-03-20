from classifier import Classifier

import sys


def main():
    # # Zadanie 1
    #
    # string1 = "Python 2023"
    # string2 = "Python 2023"
    # string3 = string1
    #
    # print(string1 == string2)  # True
    # print(string2 == string3)  # True
    #
    # print(type(string1), hex(id(string1)))  # <class 'str'> 0x7f9c0b0d3c80
    # print(type(string2), hex(id(string2)))  # <class 'str'> 0x7f9c0b0d3c80
    # print(type(string3), hex(id(string3)))  # <class 'str'> 0x7f9c0b0d3c80
    #
    # string3 = "Java 11"
    #
    # print(type(string1), hex(id(string1)))  # <class 'str'> 0x7f9c0b0d3c80
    # print(type(string2), hex(id(string2)))  # <class 'str'> 0x7f9c0b0d3c80
    # print(type(string3), hex(id(string3)))  # <class 'str'> 0x7f9c0b0d3d80
    #
    # # Zadanie 2
    #
    # num1 = float(input("Podaj pierwszą liczbę: "))
    # num2 = float(input("Podaj drugą liczbę: "))
    # operator = input("Podaj operator (+, -, *, /): ")
    #
    # if operator == "+":
    #     print(num1 + num2)
    # elif operator == "-":
    #     print(num1 - num2)
    # elif operator == "*":
    #     print(num1 * num2)
    # elif operator == "/":
    #     if num2 == 0:
    #         print("Nie można dzielić przez zero!")
    #     else:
    #         print(num1 / num2)
    # else:
    #     print("Niepoprawny operator!")

    # Zadanie ankieta
    pytania = {
        'Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:': ['a) Oglądanie telewizji',
                                                                           'b) Korzystanie z Internetu',
                                                                           'c) Czytanie książek'],
        'W jakich okolicznościach czytasz książki najczęściej?': ['a) Podczas pracy/nauki (to ich element)',
                                                                  'b) Wieczorem przed snem',
                                                                  'c) W drodze do pracy/szkoły'],
        'Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?': ['a) Czytam dla relaksu',
                                                                                                'b) Czytam dla '
                                                                                                'poszerzenia wiedzy',
                                                                                                'c) Czytam dla '
                                                                                                'zabicia czasu']
    }

    odpowiedzi = {}

    name = input('Jak masz na imię oraz nazwisko? ')

    for pytanie, mozliwe_odpowiedzi in pytania.items():
        print(pytanie)
        for odp in mozliwe_odpowiedzi:
            print(odp)
        odpowiedz = ''
        while odpowiedz not in ['a', 'b', 'c']:
            odpowiedz = input('Wybierz odpowiedź (a, b, c): ')
        odpowiedzi[pytanie] = mozliwe_odpowiedzi[ord(odpowiedz) - 97]

    print('\nOto wybrane odpowiedzi:')
    for pytanie, odpowiedz in odpowiedzi.items():
        print(pytanie)
        print('odpowiedź:', odpowiedz)


if __name__ == '__main__':
    main()

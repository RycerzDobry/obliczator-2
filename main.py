# coding=UTF-8

import colorama
import time
colorama.init()

while True:
  print('\033[36m'+'OBLICZATOR'+'\033[39m')
  time.sleep(2)
  print('aby obliczyć pole trójkąta wpisz 1')
  time.sleep(0.25)
  print('aby obliczyć pole trapezu wpisz 2')
  time.sleep(0.25)
  print('aby obliczyć pole koła wpisz 3')
  time.sleep(0.25)
  WYBOR = input('TWÓJ WYBÓR: ')
  if int(WYBOR) == 1:
    print('wybrałeś/wybrałaś obliczator pola trójkąta')
    time.sleep(2)
    print('\033[31m' + 'wczytywanie kodów atomowych...' + '\033[39m')
    time.sleep(3)
    a = input('podaj bok a: ')
    time.sleep(0.5)
    b = input('podaj bok b: ')
    time.sleep(0.5)
    h = input('podaj wysokość: ')
    wynik = (int(a) + int(b)) * int(h) / 2
    time.sleep(2)
    print('wynik: ''\033[32m' + str(wynik) + '\033[39m')
    time.sleep(1)
    print('czy chcesz zamknąć program? t/n')
    zamykanie_1 = input()
    if zamykanie_1 == "t":
      break
    elif zamykanie_1 == "n":
      continue
  elif int(WYBOR) == 2:
    print('wybrałeś/wybrałaś obliczator pola trapezu')
    time.sleep(2)
    print('\033[31m' + 'wczytywanie kodów atomowych...' + '\033[39m')
    time.sleep(3)
    a2 = input('podaj pierwszą podstawę: ')
    time.sleep(0.5)
    b2 = input('podaj drugą podstawę: ')
    time.sleep(0.5)
    h2 = input('podaj wysokość: ')
    wynik2 = (int(a2) + int(b2)) * int(h2) / 2
    time.sleep(2)
    print('wynik: ''\033[32m' + str(wynik2) + '\033[39m')
    time.sleep(1)
    print('czy chcesz zamknąć program? t/n')
    zamykanie_2 = input()
    if zamykanie_2 == 't':
      break
    elif zamykanie_2 == "n":
      continue
  elif int(WYBOR) == 3:
    print('wybrałeś/wybrałaś obliczator pola koła')
    time.sleep(2)
    print('\033[31m' + 'wczytywanie kodów atomowych...' + '\033[39m')
    time.sleep(3)
    r = input('podaj promień: ')
    wynik3 = 3.14 * int(r)**2
    print('wynik: ' + '\033[32m' + str(wynik3) + '\033[39m')
    time.sleep(1)
    print('czy chcesz zamknąć program? t/n')
    zamykanie_3 = input()
    t = 't'
    n = 'n'
    if zamykanie_3 == "t":
      break
    elif zamykanie_3 == "n":
      continue

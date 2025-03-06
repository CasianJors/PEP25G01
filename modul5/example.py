# import

import random

print(random.choice('abcd'))
print(random.choice([1, 2, 3, 4, 5]))
print(random.randint(10000, 20000))

import random as r

print(r.choice('abcd'))

print('Name of this script is: ', __name__)

from modul4.seminar1.app1 import check_parola

password = "test"
check_parola(password)

from modul4.seminar2 import example
from modul4.seminar2 import app1

print(example.my_set1)
print('Calcul varsta medie: ', app1.medie([10,22,15]))
print('Media este: ', app1.suma([1, 2]))

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
not_primes = []
primes = []
for i in numbers:    #  перебираем список
    if i == 1:
        continue
    is_prime = True  # отмечаем простые числа
    for j in range(2,i):     #  перебираем список и подбераем делитель
        if (i%j) == 0:       #  сравниваем результат

            not_primes.append(i)
            break
        is_prime = False     #  отмечаем  не простые числа
    else:
        primes.append(i)
print(f'Primes{primes}')
print(f'Not_primes{not_primes}')

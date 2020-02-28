'''Решето Эратосфена - функция возвращает список простых до указанного n включительно.'''

def erato(n):

    sieve = [i for i in range(n+1)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i
    result = [i for i in sieve if i != 0]
    return result

print(erato(29))
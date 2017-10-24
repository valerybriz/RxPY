import time
import concurrent.futures
import rx
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]
start_time = time.time()

def is_prime(n):

    if n % 2 == 0:
        return str(n) +" False " + str(time.time() - start_time)

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return str(n) +" False "  + str(time.time() - start_time)
    return str(n) +" True " +  str(time.time() - start_time)

def main():

    with concurrent.futures.ProcessPoolExecutor(6) as worker:
        rx.Observable.from_(PRIMES).flat_map(
            lambda num: worker.submit(is_prime, num)
            ).subscribe(print)

if __name__ == '__main__':
    main()

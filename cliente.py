from rpc import Client
import time


def main():
    client = Client('localhost', 45000)

    print(client.soma(10, 'a'))
    print(client.sub(10, 20, 30))
    print(client.mult(10, 10, 2))
    print(client.div(20, 5, 2, 0))
    print(client.soma())
    print(client.mult(-1.33, -5.22, 10.893173))
    print(client.is_prime(10))
    print(client.is_prime(13))
    print(client.is_prime(1))
    print(client.is_prime(-2))
    print(client.is_prime(10, 20, 30, 13, 17))
    print(client.is_prime(10, 20, 30, 13, 17))

    # t1 = time.time()
    # client.show_primes_in_range(1, 100000)
    # print(f'Tempo execução: {time.time() - t1}s')


    # t2 = time.time()
    # client.mp_show_primes_in_range(1, 100000)
    # print(f'Tempo execução: {time.time()-t2}s')

if __name__ == '__main__':
    main()

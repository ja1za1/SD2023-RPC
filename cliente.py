from rpc.cliente.Client import Client


def main():
    client = Client('localhost', 38500)
    # print(client.sum(19.2, 15.3))
    # print(client.sub(7.3, 5.3))
    # print(client.mult(7,2,25))
    # print(client.div(30,2,5))
    # print(client.is_prime(1,2,3,4,5))
    # print(client.is_prime(7))
    print(client.show_primes_in_range_mp(1, 50))
    # print(client.show_primes_in_range(1, 1000))
    # print(client.show_primes_in_range(1, 1000))
    # print(client.is_prime(1))
    # print(client.last_news_if_barbacena(1))
    print(client.last_news_if_barbacena(20))
    # print(client.last_news_if_barbacena(5)[0])
    # print(client.soma(100000, 100000))
    # time.sleep(3)
    # print(client.soma(10002, 100000))

    # print(client.soma(50, 50))
    # time.sleep(3)
    # print(client.mult(10, 20))
    # time.sleep(3)
    # print(client.mp_show_primes_in_range(1,1000))
    # time.sleep(3)
    # print(client.mp_show_primes_in_range(1,20))
    # print(client.sub(10, 20, 30))
    # print(client.mult(10, 10, 2))
    # print(client.div(20, 5, 2, 0))
    # print(client.soma())
    # print(client.mult(-1.33, -5.22, 10.893173))
    # print(client.is_prime(10))
    # print(client.is_prime(13))
    # print(client.is_prime(1))
    # print(client.is_prime(-2))
    # print(client.is_prime(10, 20, 30, 13, 17))
    # print(client.is_prime(10, 20, 30, 13, 17))

    # t1 = time.time()
    # client.mp_show_primes_in_range(1, 100000)
    # print(f'Tempo execução 1: {time.time() - t1:.15f}s')


    # t2 = time.time()
    # client.mp_show_primes_in_range(1, 100000)
    # print(f'Tempo execução 2: {time.time() - t2:.15f}s')

if __name__ == '__main__':
    main()

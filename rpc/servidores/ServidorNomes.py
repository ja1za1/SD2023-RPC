import socket
import threading
import json


class ServidorNomes:

    IP = 'localhost'
    PORTA = 38500
    BUFFER_SIZE = 4096

    SERVIDORES = {
        'sum' : (('localhost', 45000),),
        'sub' : (('localhost', 45000),),
        'mult' : (('localhost', 45000),),
        'div' : (('localhost', 45000),),
        'is_prime' : (('localhost', 45000),),
        'show_primes_in_range' : (('localhost', 45000),),
        'show_primes_in_range_mp' : (('localhost', 45000),),
        'last_news_if_barbacena' : (('localhost', 45000),)
    }

    def __init__(self) -> None:
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__socket.bind((self.IP, self.PORTA))
        print(f'Servidor iniciado no IP: {self.IP}, PORTA: {self.PORTA}')

    def iniciar(self):
        while True:
            dados, cliente = self.__socket.recvfrom(self.BUFFER_SIZE)
            thread = threading.Thread(target=self.__identificar_servidor_operacao, args=(cliente,dados))
            thread.start()
          

    def __identificar_servidor_operacao(self, ip_cliente, dados_recebidos_cliente):
        nome_operacao = dados_recebidos_cliente.decode()
        if nome_operacao in self.SERVIDORES:
            self.__socket.sendto(json.dumps({'resp': self.SERVIDORES[nome_operacao]}).encode(), ip_cliente)
        else:
            self.__socket.sendto(json.dumps({'resp': ()}).encode(), ip_cliente)
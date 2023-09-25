import socket
import json

from rpc.Cache import Cache

BUFFER_SIZE = 4096

class Client:

    def __init__(self, ip, porta) -> None:
        self.ip = ip
        self.porta = porta
        self._socket = self.__conectar_servidor(ip,porta)
        self.__cache = Cache()
    
    def __del__(self):
        self.__cache.escrever_cache_disco()
        self.__cache.escrever_lista_operacoes_disco()
        
    def __conectar_servidor(self,ip, porta) -> socket.socket:
        socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketCliente.connect((ip,porta))
        return socketCliente
    
    def __enviar_operacao_servidor(self,dadosOperacao) -> None:
        self._socket.send(dadosOperacao.encode())

    def __obter_resposta_servidor(self, dadosOperacao):
        resposta_servidor = bytearray()

        while True:
            data = self._socket.recv(BUFFER_SIZE)
            if not data:
                break
            resposta_servidor += data

            if len(data) < BUFFER_SIZE:
                break
        resposta_servidor = json.loads(data.decode())['resp']
        self.__cache.armazenar_dados_cache(dadosOperacao, resposta_servidor)
        return resposta_servidor
    
    def __verificar_resposta_em_cache(self,dados_operacao):
        return self.__cache.obter_dados_em_cache(dados_operacao)
        
    def soma(self, *numeros) -> float:
        dadosOperacao = 'soma'
        for numero in numeros:
            dadosOperacao += f' {numero}'
        resposta_operacao = self.__verificar_resposta_em_cache(dadosOperacao)
        if resposta_operacao != None:
            return resposta_operacao
        else:
            self.__enviar_operacao_servidor(dadosOperacao)
            return self.__obter_resposta_servidor(dadosOperacao)
    
    def sub(self, *numeros) -> float:
        dadosOperacao = 'sub'
        for numero in numeros:
            dadosOperacao += f' {numero}'
        resposta_operacao = self.__verificar_resposta_em_cache(dadosOperacao)
        if resposta_operacao != None:
            return resposta_operacao
        else:
            self.__enviar_operacao_servidor(dadosOperacao)
            return self.__obter_resposta_servidor(dadosOperacao)

    def mult(self, *numeros) -> float:
        dadosOperacao = 'mult'
        for numero in numeros:
            dadosOperacao += f' {numero}'
        resposta_operacao = self.__verificar_resposta_em_cache(dadosOperacao)
        if resposta_operacao != None:
            return resposta_operacao
        else:
            self.__enviar_operacao_servidor(dadosOperacao)
            return self.__obter_resposta_servidor(dadosOperacao)
    
    def div(self, *numeros) -> float:
        dadosOperacao = 'div'
        for numero in numeros:
            if numero == 0:
                return 'Divsão por 0 não é possível'
            dadosOperacao += f' {numero}'
        resposta_operacao = self.__verificar_resposta_em_cache(dadosOperacao)
        if resposta_operacao != None:
            return resposta_operacao
        else:
            self.__enviar_operacao_servidor(dadosOperacao)
            return self.__obter_resposta_servidor(dadosOperacao)
    
    def is_prime(self, *numeros) -> bool:
        dadosOperacao = 'num_primo'
        for numero in numeros:
            if not isinstance(numero, int):
                raise TypeError("Número deve ser inteiro")
            else:
                dadosOperacao += f' {numero}'
        resposta_operacao = self.__verificar_resposta_em_cache(dadosOperacao)
        if resposta_operacao != None:
            return resposta_operacao
        else:
            self.__enviar_operacao_servidor(dadosOperacao)
            return self.__obter_resposta_servidor(dadosOperacao)
    
    def show_primes_in_range(self, inicio, fim):
        dadosOperacao = 'primos_range'
        if not isinstance(inicio, int) or not isinstance(fim, int):
            raise TypeError("Número deve ser inteiro")
        else:
            dadosOperacao += f' {inicio} {fim}'
            resposta_operacao = self.__verificar_resposta_em_cache(dadosOperacao)
            if resposta_operacao != None:
                return resposta_operacao
            else:
                self.__enviar_operacao_servidor(dadosOperacao)
                return self.__obter_resposta_servidor(dadosOperacao)
    
    def show_primes_in_range_mp(self, inicio, fim):
        dadosOperacao = 'primos_range_mp'
        if not isinstance(inicio, int) or not isinstance(fim, int):
            raise TypeError("Número deve ser inteiro")
        else:
            dadosOperacao += f' {inicio} {fim}'
            resposta_operacao = self.__verificar_resposta_em_cache(dadosOperacao)
            if resposta_operacao != None:
                return resposta_operacao
            else:
                self.__enviar_operacao_servidor(dadosOperacao)
                return self.__obter_resposta_servidor(dadosOperacao)
            
    def last_news_if_barbacena(self, qtd_noticias : int) -> list:
        dadosOperacao = f'news {qtd_noticias}'
        resposta_operacao = self.__verificar_resposta_em_cache(dadosOperacao)
        if resposta_operacao != None:
            return resposta_operacao
        else:
            self.__enviar_operacao_servidor(dadosOperacao)
            return self.__obter_resposta_servidor(dadosOperacao)
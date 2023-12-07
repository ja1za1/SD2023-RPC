import socket
import json
import time
import inspect
import ssl

from random import randint
from rpc.cliente.Cache import Cache
from rpc.servidores.ConectarServidorNomes import ConectarServidorNomes
from rpc.excecoes.ServidorDesligadoException import ServidorDesligadoException 

BUFFER_SIZE = 4096

class Client:

    def __init__(self, ip, porta) -> None:
        self.ip = ip
        self.porta = porta
        self.__socket_servidor_nomes = ConectarServidorNomes(ip, porta)
        self.__cache = Cache()
    
    def __del__(self):
        self.__cache.escrever_cache_disco()
        self.__cache.escrever_lista_operacoes_disco()
        
    def __conectar_servidor(self,ip, porta) -> ssl.SSLSocket:
        try:
            self.SSL_CONTEXT = ssl.create_default_context()
            self.SSL_CONTEXT.load_verify_locations("./ssl/device.crt")
            self.SSL_CONTEXT.check_hostname = False
            self.SSL_CONTEXT.verify_mode = ssl.CERT_NONE
            socketCliente = self.SSL_CONTEXT.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=ip)
            socketCliente.connect((ip,porta))
            return socketCliente
        except socket.timeout:
            return None
        except ConnectionRefusedError:
            return None
        
    
    def __enviar_operacao_servidor(self,dadosOperacao) -> bool:
        nome_operacao = dadosOperacao.split(" ")[0]
        try:
            self.__socket = None
            servidores_contendo_operacao = self.__socket_servidor_nomes.obter_nome_servidor(nome_operacao)
            print(servidores_contendo_operacao)
            while len(servidores_contendo_operacao) > 0 :
                servidor = servidores_contendo_operacao.pop(randint(0, len(servidores_contendo_operacao)-1))
                print(servidor)
                socketServidor = self.__conectar_servidor(*servidor)
                if socketServidor != None:
                    self.__socket = socketServidor
                    self.__socket.send(dadosOperacao.encode())
                    return True
                    
            if self.__socket == None:
                print("nao conectou servidor")
                return False
        except ServidorDesligadoException:
            return False

    def __obter_resposta_servidor(self, dadosOperacao):
        resposta_servidor = bytearray()

        while True:
            data = self.__socket.recv(BUFFER_SIZE)
            time.sleep(0.5)
            if not data:
                break
            resposta_servidor += data

            if len(data) < BUFFER_SIZE:
                break 
        resposta_servidor = json.loads(resposta_servidor.decode())['resp']
        self.__cache.armazenar_dados_cache(dadosOperacao, resposta_servidor)
        return resposta_servidor
    
    def __verificar_resposta_em_cache(self,dados_operacao):
        return self.__cache.obter_dados_em_cache(dados_operacao)
    
    def __realizar_operacao(self, parametros):
        nome_operacao = inspect.stack()[1].function
        operacao = f'{nome_operacao} {" ".join(map(str, parametros))}'
        print(operacao)
        resposta_operacao = self.__verificar_resposta_em_cache(operacao)
        if(resposta_operacao != None):
            return resposta_operacao
        elif self.__enviar_operacao_servidor(operacao):
            return self.__obter_resposta_servidor(operacao)
        else:
            return f'Erro ao realizar operação {operacao}'
        
    def sum(self, *numeros) -> float:
        return self.__realizar_operacao(numeros)
    
    def sub(self, *numeros) -> float:
        return self.__realizar_operacao(numeros)

    def mult(self, *numeros) -> float:
        return self.__realizar_operacao(numeros)
            
    def div(self, *numeros) -> float:
        return self.__realizar_operacao(numeros)
    
    def is_prime(self, *numeros) -> bool:
        return self.__realizar_operacao(numeros)
    
    def show_primes_in_range(self, inicio, fim):
        return self.__realizar_operacao((inicio,fim))
    
    def show_primes_in_range_mp(self, inicio, fim):
        return self.__realizar_operacao((inicio,fim))
            
    def last_news_if_barbacena(self, qtd_noticias : int) -> list:
        return self.__realizar_operacao((qtd_noticias,))
    
    def validate_cpf(self, cpf : str):
        return self.__realizar_operacao((cpf,))
    

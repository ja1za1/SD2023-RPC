import socket
import threading
import json
import datetime
import os
import ssl

from rpc.Operacoes import Operacoes as op

class Server:
    BUFFER_SIZE = 4096
    OPERACOES = {
        'sum' : op.soma,
        'sub' : op.subtracao,
        'mult' : op.multiplicacao,
        'div' : op.divisao,
        'is_prime' : op.numeros_primos,
        'show_primes_in_range' : op.primos_range,
        'show_primes_in_range_mp' : op.primos_range_mp,
        'last_news_if_barbacena' : op.buscar_noticias_barbacena,
        'validate_cpf' : op.validate_cpf
    }
 

    def __init__(self, ip, porta) -> None:
        self.ip = ip
        self.porta = porta
        self.LOG_FILE = f"./logs/log-{ip}.txt"

    def iniciar(self) -> None:
        socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.SSL_CONTEXT = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        self.SSL_CERTIFILE = "./ssl/rootCA.pem"
        self.SSL_KEYFILE = "./ssl/rootCA.key"
        self.SSL_CONTEXT.load_cert_chain(certfile=self.SSL_CERTIFILE, keyfile=self.SSL_KEYFILE)
        socketServer.bind((self.ip, self.porta))
        socketServer.listen()
        print(f'Servidor iniciado no IP: {self.ip}, PORTA: {self.porta}')
        while True:
            try:
                conexao_cliente, addr = socketServer.accept()
                print(f'Cliente conectado: {addr}')
                thread = threading.Thread(target=self.__realizar_operacao, args=(conexao_cliente,))
                thread.start()
            except KeyboardInterrupt:
                break

    def __obter_nome_operacao(self, dados_operacao) -> str:
        return dados_operacao.split(' ')[0]
    
    def __obter_parametros_operacao(self, dados_operacao) -> list:
        params = []
        for n in dados_operacao.split(' ')[1:]:
            params.append(n)

        return params
        
    def __realizar_operacao(self,conexao_cliente) -> None:
        while True:
            if(conexao_cliente.fileno() == - 1):
                break
            with self.SSL_CONTEXT.wrap_socket(conexao_cliente, server_side=True) as conexao_segura:
            
                dados_operacao = conexao_segura.recv(self.BUFFER_SIZE).decode()
                if not dados_operacao:
                    break
                
                tempo_inicial = datetime.datetime.now()
                operacao = self.__obter_nome_operacao(dados_operacao)
                parametros = self.__obter_parametros_operacao(dados_operacao)
                
                # Chamada da função através da chave do dicionário.
                resultado = self.OPERACOES[operacao](parametros)
                self.__enviar_resultado_cliente(conexao_segura,resultado)
                tempo_final = datetime.datetime.now() - tempo_inicial
                self.__gerar_log(conexao_segura.getpeername(), operacao, tempo_final.microseconds/1000)
    
    def __enviar_resultado_cliente(self, conexaoCliente, resultado) -> None:
        conexaoCliente.send(json.dumps({'resp': resultado}).encode())

    def __gerar_log(self, conexao_cliente, operacao, tempo_resposta):
        with open(self.LOG_FILE, 'a+') as arquivo:
            arquivo.write(f'{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")},{conexao_cliente[0]},{operacao},{tempo_resposta}ms\n')
            
            
            
        
    
import socket
import threading
import json

from rpc.Operacoes import Operacoes as op

class Server:
    BUFFER_SIZE = 4096
    OPERACOES = {
        'soma' : op.soma,
        'sub' : op.subtracao,
        'mult' : op.multiplicacao,
        'div' : op.divisao,
        'num_primo' : op.numeros_primos,
        'primos_range_mp' : op.primos_range_mp,
        'primos_range' : op.primos_range,
        'news' : op.buscar_noticias_barbacena

    }

    def __init__(self, ip, porta) -> None:
        self.ip = ip
        self.porta = porta

    def iniciar(self) -> None:
        socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        socketServer.bind((self.ip, self.porta))
        socketServer.listen()
        print(f'Servidor iniciado no IP: {self.ip}, PORTA: {self.porta}')
        while True:
            try:
                conexaoCliente, addr = socketServer.accept()
                print(f'Cliente conectado: {addr}')
                thread = threading.Thread(target=self.__realizar_operacao, args=(conexaoCliente,))
                thread.start()
            except KeyboardInterrupt:
                break

    def __obter_nome_operacao(self, dadosOperacao) -> str:
        return dadosOperacao.split(' ')[0]
    
    def __obter_parametros_operacao(self, dadosOperacao) -> list:
        params = []
        for n in dadosOperacao.split(' ')[1:]:
            params.append(float(n))
        return params
        
    def __realizar_operacao(self,conexaoCliente) -> None:
        while True:
            dadosOperacao = conexaoCliente.recv(self.BUFFER_SIZE).decode()
            if not dadosOperacao:
                break
            
            operacao = self.__obter_nome_operacao(dadosOperacao)
            parametros = self.__obter_parametros_operacao(dadosOperacao)

            # Chamada da função através da chave do dicionário.
            resultado = self.OPERACOES[operacao](parametros)
            self.__enviar_resultado_cliente(conexaoCliente,resultado) 
    
    def __enviar_resultado_cliente(self, conexaoCliente, resultado) -> None:
        conexaoCliente.send(json.dumps({'resp': resultado}).encode())

    
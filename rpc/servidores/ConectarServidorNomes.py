import socket
import json
from rpc.excecoes.ServidorDesligadoException import ServidorDesligadoException

class ConectarServidorNomes:

    BUFFER_SIZE = 4096
    TIMEOUT = 2

    def __init__(self, ip, porta) -> None:
        self.__ip = ip
        self.__porta = porta
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        


    def obter_nome_servidor(self, nome_operacao):
        return self.__obter_endereco_servidor_nomes(nome_operacao)


    def __obter_endereco_servidor_nomes(self, nome_operacao):

        self.__socket.sendto(nome_operacao.encode(), (self.__ip, self.__porta))
        return self.__obter_resposta_servidor_nomes()
        

    def __obter_resposta_servidor_nomes(self):
        try:
            data = bytearray()
            while True:
                self.__socket.settimeout(self.TIMEOUT)
                msg = self.__socket.recv(self.BUFFER_SIZE)
                if not msg:
                    break
                data += msg
                if len(data) < self.BUFFER_SIZE:
                    break
            return json.loads(data.decode())['resp']
        except socket.timeout:
            raise ServidorDesligadoException("Erro ao obter endereço do servidor contendo operação")
       
import socket
import threading
import os
import multiprocessing as mp
from functools import reduce
from typing import List

BUFFER_SIZE = 1024

class Client:
    def __init__(self, ip, porta) -> None:
        self.ip = ip
        self.porta = porta
        self._socket = self._conectarServidor(ip,porta)
        self._cache = {}

    def _conectarServidor(self,ip, porta) -> socket.socket:
        socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketCliente.connect((ip,porta))
        return socketCliente
    
    def _armazenarRespostaCache(self,dadosOperacao, resposta_servidor):
        self._cache[dadosOperacao] = resposta_servidor
    
    def _enviarOperacaoServidor(self,dadosOperacao) -> None:
        self._socket.send(dadosOperacao.encode())

    def _obterRespostaServidor(self, dadosOperacao):
        resposta_servidor = b""

        while True:
            data = self._socket.recv(BUFFER_SIZE)
            if not data:
                break
            resposta_servidor += data

            if len(data) < BUFFER_SIZE:
                break
        resposta_servidor = resposta_servidor.decode('utf-8')
        self._armazenarRespostaCache(dadosOperacao, resposta_servidor)
        return resposta_servidor
    
    def _obterOperacaoEmCache(self, dadosOperacao):
        if dadosOperacao in self._cache:
            return self._cache[dadosOperacao]
        else:
            return None

    def soma(self, *numeros) -> float:
        dadosOperacao = 'soma'
        for numero in numeros:
            dadosOperacao += f' {numero}'
        resposta_operacao = self._obterOperacaoEmCache(dadosOperacao)
        if resposta_operacao != None:
            return resposta_operacao
        else:
            self._enviarOperacaoServidor(dadosOperacao)
            return self._obterRespostaServidor(dadosOperacao)
    
    def sub(self, *numeros) -> float:
        dadosOperacao = 'sub'
        for numero in numeros:
            dadosOperacao += f' {numero}'
        resposta_operacao = self._obterOperacaoEmCache(dadosOperacao)
        if resposta_operacao != None:
            return resposta_operacao
        else:
            self._enviarOperacaoServidor(dadosOperacao)
            return self._obterRespostaServidor(dadosOperacao)

    def mult(self, *numeros) -> float:
        dadosOperacao = 'mult'
        for numero in numeros:
            dadosOperacao += f' {numero}'
        resposta_operacao = self._obterOperacaoEmCache(dadosOperacao)
        if resposta_operacao != None:
            return resposta_operacao
        else:
            self._enviarOperacaoServidor(dadosOperacao)
            return self._obterRespostaServidor(dadosOperacao)
    
    def div(self, *numeros) -> float:
        dadosOperacao = 'div'
        for numero in numeros:
            if numero == 0:
                return 'Divsão por 0 não é possível'
            dadosOperacao += f' {numero}'
        resposta_operacao = self._obterOperacaoEmCache(dadosOperacao)
        if resposta_operacao != None:
            return resposta_operacao
        else:
            self._enviarOperacaoServidor(dadosOperacao)
            return self._obterRespostaServidor(dadosOperacao)
    
    def is_prime(self, *numeros) -> bool:
        dadosOperacao = 'num_primo'
        for numero in numeros:
            if not isinstance(numero, int):
                raise TypeError("Número deve ser inteiro")
            else:
                dadosOperacao += f' {numero}'
        resposta_operacao = self._obterOperacaoEmCache(dadosOperacao)
        if resposta_operacao != None:
            return resposta_operacao
        else:
            self._enviarOperacaoServidor(dadosOperacao)
            return self._obterRespostaServidor(dadosOperacao)
    
    def show_primes_in_range(self, inicio, fim):
        primos = []
        for i in range(inicio,fim):
            primo = self.is_prime(i)
            if primo == '[True]':
                primos.append(i)
        return str(primos)
    
    def mp_show_primes_in_range(self, inicio, fim):
        dadosOperacao = 'mp_num_primo'
        if not isinstance(inicio, int) or not isinstance(fim, int):
            raise TypeError("Número deve ser inteiro")
        else:
            dadosOperacao += f' {inicio} {fim}'
            resposta_operacao = self._obterOperacaoEmCache(dadosOperacao)
            if resposta_operacao != None:
                return resposta_operacao
            else:
                self._enviarOperacaoServidor(dadosOperacao)
                return self._obterRespostaServidor(dadosOperacao)

        

        
            



class Server:
    def __init__(self, ip, porta) -> None:
        self.ip = ip
        self.porta = porta

    def _obterNomeOperacao(self, dadosOperacao) -> str:
        return dadosOperacao.split(' ')[0]
    
    def _obterNumerosFloat(self, dadosOperacao) -> List[float]:
        numeros = []
        for numero in dadosOperacao.split(' '):
            try:
                numeros.append(float(numero))
            except ValueError:
                continue
        return numeros
    
    def _obterNumerosInteiros(self, dadosOperacao) -> List[int]:
        numeros = []
        for numero in dadosOperacao.split(' '):
            try:
                numeros.append(int(numero))
            except ValueError:
                continue
        return numeros
    
    def _obterRangeNumerosInteiros(self, dadosOperacao) -> List[int]:
        inicio = int(dadosOperacao.split(' ')[1])
        fim = int(dadosOperacao.split(' ')[2])
        return list(range(inicio, fim+1))
        

    def _realizarOperacao(self,conexaoCliente) -> float:
        while True:
            dadosOperacao = conexaoCliente.recv(BUFFER_SIZE).decode()
            if not dadosOperacao:
                break
            operacao = self._obterNomeOperacao(dadosOperacao)
            resultado = ''
            if operacao == 'soma':
                numerosOperacao = self._obterNumerosFloat(dadosOperacao)
                resultado = str(sum(numerosOperacao))
            elif operacao == 'sub':
                numerosOperacao = self._obterNumerosFloat(dadosOperacao)
                resultado = str(reduce(lambda x, y: x - y, numerosOperacao))
            elif operacao == 'mult':
                numerosOperacao = self._obterNumerosFloat(dadosOperacao)
                resultado = str(reduce(lambda x, y: x * y, numerosOperacao))
            elif operacao == 'div':
                numerosOperacao = self._obterNumerosFloat(dadosOperacao)
                resultado = str(reduce(lambda x, y: x / y, numerosOperacao))
            elif operacao == 'num_primo':
                numeros = self._obterNumerosInteiros(dadosOperacao)
                resultado = str(self._verificarNumerosPrimo(numeros))
            elif operacao == 'mp_num_primo':
                numeros = self._obterRangeNumerosInteiros(dadosOperacao)
                resultado = str(self._mpVerificarNumerosPrimos(numeros))
                
            self._enviarResultadoCliente(conexaoCliente,resultado) 
    
    def _enviarResultadoCliente(self, conexaoCliente, resultado) -> None:
        conexaoCliente.send(resultado.encode())

    def _verificarNumerosPrimo(self, numeros):
        primos = []
        for num in numeros:
            primos.append(self._verificarNumeroPrimo(num))  

        return primos
    
    def _verificarNumeroPrimo(self, num):
        if num == 1:
            return False
        elif num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
        else:
            return False
        
        return True
    
    def _mpVerificarNumerosPrimos(self, lista_numeros):
            with mp.Pool(processes=os.cpu_count()) as pool:
                results = pool.map(self._verificarNumeroPrimo, lista_numeros)
                prime_numbers = [number[0] for number in zip(lista_numeros, results) if number[1]]
                return prime_numbers



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
                thread = threading.Thread(target=self._realizarOperacao, args=(conexaoCliente,))
                thread.start()
            except KeyboardInterrupt:
                break
    


import multiprocessing as mp
import os
import concurrent.futures

from functools import reduce
from rpc.Webscrapping import get_links
from math import ceil

class Operacoes:
    
    @staticmethod
    def soma(numeros : list = [0]):
        return sum(numeros)

    @staticmethod
    def subtracao(numeros : list = [0]):
        return reduce(lambda x, y: x - y, numeros)

    @staticmethod
    def multiplicacao(numeros : list = [0]):
        return reduce(lambda x, y: x * y, numeros)

    @staticmethod
    def divisao(numeros: list = [0]):
        return reduce(lambda x, y: x / y, numeros)
    

    @staticmethod
    def numeros_primos(numeros: list = [0]):
        primos = []
        for num in numeros:
            primos.append(Operacoes.numero_primo(int(num)))
        return primos

    @staticmethod
    def numero_primo(numero: int = 1):
        if numero == 1:
            return False
        elif numero > 1:
            for i in range(2, numero):
                if (numero % i) == 0:
                    return False
        else:
            return False
        
        return True

    @staticmethod
    def primos_range(rangePrimos: list = [0]):
        inicio = int(rangePrimos[0])
        fim = int(rangePrimos[1])
        lista_numeros = range(inicio, fim+1)
        numeros_primos = []
        for numero in lista_numeros:
            if(Operacoes.numero_primo(numero)):
                numeros_primos.append(numero)
        return numeros_primos
    
    
    @staticmethod
    def primos_range_mp(rangePrimos: list = [0]):
        inicio = int(rangePrimos[0])
        fim = int(rangePrimos[1])
        lista_numeros = range(inicio, fim+1)
        with mp.Pool(processes=os.cpu_count()) as pool:
                resultado = pool.map(Operacoes.numero_primo, lista_numeros)
                numeros_primos = [number[0] for number in zip(lista_numeros, resultado) if number[1]]
        return numeros_primos

    @staticmethod
    def buscar_noticias_barbacena(qtdNoticias: list = [0]):
        QUANTIDADE_NOTICIAS = int(qtdNoticias[0])
        QUANTIDADE_NOTICIAS_PAGINA = 20
        ITERACOES_SCRAPPING = ceil(QUANTIDADE_NOTICIAS / QUANTIDADE_NOTICIAS_PAGINA)
        
        noticias = []
        urls = []
        
        for i in range(ITERACOES_SCRAPPING):
            urls.append(f'https://www.ifsudestemg.edu.br/noticias/barbacena/?b_start:int={i * QUANTIDADE_NOTICIAS_PAGINA}')
            
        with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
            for lista_noticia in executor.map(get_links, urls):
                if lista_noticia:
                    noticias += lista_noticia
                    
        return noticias[0:QUANTIDADE_NOTICIAS]







        

import multiprocessing as mp
import os
import concurrent.futures
import re

from functools import reduce
from rpc.Webscrapping import get_links
from math import ceil

class Operacoes:
    
    @staticmethod
    def soma(numeros : list = [0]):
        numeros = [float(x) for x in numeros]
        return sum(numeros)

    @staticmethod
    def subtracao(numeros : list = [0]):
        numeros = [float(x) for x in numeros]
        return reduce(lambda x, y: x - y, numeros)

    @staticmethod
    def multiplicacao(numeros : list = [0]):
        numeros = [float(x) for x in numeros]
        return reduce(lambda x, y: x * y, numeros)

    @staticmethod
    def divisao(numeros: list = [0]):
        numeros = [float(x) for x in numeros]
        return reduce(lambda x, y: x / y, numeros)
    

    @staticmethod
    def numeros_primos(numeros: list = [0]):
        numeros = [float(x) for x in numeros]
        primos = []
        for num in numeros:
            primos.append(Operacoes.numero_primo(int(num)))
        return primos

    @staticmethod
    def numero_primo(numero: int = 1):
        numero = int(numero)
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
        rangePrimos = [float(x) for x in rangePrimos]
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
        rangePrimos = [float(x) for x in rangePrimos]
        inicio = int(rangePrimos[0])
        fim = int(rangePrimos[1])
        lista_numeros = range(inicio, fim+1)
        with mp.Pool(processes=os.cpu_count()) as pool:
                resultado = pool.map(Operacoes.numero_primo, lista_numeros)
                numeros_primos = [number[0] for number in zip(lista_numeros, resultado) if number[1]]
        return numeros_primos

    @staticmethod
    def buscar_noticias_barbacena(qtdNoticias: list = [0]):
        qtdNoticias = [float(x) for x in qtdNoticias]
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
    
    @staticmethod
    def validate_cpf(cpf: list) -> bool:
        cpf = cpf[0]
        """ Efetua a validação do CPF, tanto formatação quando dígito verificadores.

        Parâmetros:
            cpf (str): CPF a ser validado

        Retorno:
            bool:
                - Falso, quando o CPF possuir o formato 999.999.999-99;
                - Falso, quando o CPF não possuir 11 caracteres numéricos;
                - Falso, quando os dígitos verificadores forem inválidos;
                - Verdadeiro, caso contrário.

        Exemplos:

        >>> validate('529.982.247-25')
        False
        >>> validate('111.111.111-11')
        False
        >>> validate('52998224725')
        True
        """

        # Verifica a formatação do CPF
        if not re.match(r'\d{3}\d{3}\d{3}\d{2}', cpf):
            return False

        # Obtém apenas os números do CPF, ignorando pontuações
        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        # Verifica se o CPF possui 11 números ou se todos são iguais:
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        # Validação do primeiro dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        # Validação do segundo dígito verificador:
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return True







        
import pickle
import os

from datetime import datetime

class Cache:

    TEMPO_MIN_SINCRONIZACAO_CACHE = 2
    NUMERO_MAX_REGISTROS = 5
    NOME_PASTA_CACHE = './cache/'
    NOME_ARQUIVO_CACHE = f'{NOME_PASTA_CACHE}cache.pk'
    NOME_LISTA_OPERACOES = f'{NOME_PASTA_CACHE}.lista_operacoes.pk'

    def __init__(self) -> None:
        self.__cache = self.__carregar_cache_disco()
        self.__lista_operacoes = self.__carregar_lista_operacoes()
        self.__horario_ultima_requisicao = datetime.now().timestamp()

    def __carregar_cache_disco(self):
        try:
            cache_disco = pickle.load(open(self.NOME_ARQUIVO_CACHE, 'rb'))
        except:
            cache_disco = {}
            
        return cache_disco
    
    def __carregar_lista_operacoes(self):
        try:
            lista_op = pickle.load(open(self.NOME_LISTA_OPERACOES, 'rb'))
        except:
            lista_op = []

        return lista_op
    
    def __lista_op_cheia(self):
        return len(self.__lista_operacoes) == self.NUMERO_MAX_REGISTROS
    
    def __inserir_dados_lista_operacoes(self, dados_inserir):
        if(self.__lista_op_cheia()):
            operacao_mais_antiga = self.__lista_operacoes.pop(0)
            del self.__cache[operacao_mais_antiga]
        self.__lista_operacoes.append(dados_inserir)

    def __verificar_tempo_sincronizacao_cache(self):
        if datetime.now().timestamp() - self.__horario_ultima_requisicao >= self.TEMPO_MIN_SINCRONIZACAO_CACHE:
            self.__horario_ultima_requisicao = datetime.now().timestamp()
            self.escrever_cache_disco()
            self.escrever_lista_operacoes_disco()
    
    def armazenar_dados_cache(self, chave, valor):
        self.__cache[chave] = valor
        self.__inserir_dados_lista_operacoes(chave)
        self.__verificar_tempo_sincronizacao_cache()

    def escrever_cache_disco(self):
        os.makedirs(os.path.dirname(self.NOME_PASTA_CACHE), exist_ok=True)
        with open(self.NOME_ARQUIVO_CACHE, 'wb') as arquivo_cache:    
            pickle.dump(self.__cache, arquivo_cache)
        
    def escrever_lista_operacoes_disco(self):
        os.makedirs(os.path.dirname(self.NOME_PASTA_CACHE), exist_ok=True)
        with open(self.NOME_LISTA_OPERACOES, 'wb') as arquivo_lista_op:    
            pickle.dump(self.__lista_operacoes, arquivo_lista_op)

    def obter_dados_em_cache(self, chave):
        if chave in self.__cache:
            return self.__cache[chave]
        else:
            return None

    


    

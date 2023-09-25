import pickle
import os

from datetime import datetime

class Cache:

    TEMPO_MIN_SINCRONIZACAO_CACHE = 2 # SEGUNDOS
    NUMERO_MAX_REGISTROS = 5
    TEMPO_ATUALIZACAO_CACHE_NOTICIAS = 300 # SEGUNDOS
    NOME_PASTA_CACHE = './cache/'
    NOME_ARQUIVO_CACHE = f'{NOME_PASTA_CACHE}cache.pk'
    NOME_LISTA_OPERACOES = f'{NOME_PASTA_CACHE}.lista_operacoes.pk'

    def __init__(self) -> None:
        self.__horario_ultima_atualizacao = 0
        self.__cache = self.__carregar_cache_disco()
        self.__lista_operacoes = self.__carregar_lista_operacoes()

    def __carregar_cache_disco(self):
        try:
            cache_disco = pickle.load(open(self.NOME_ARQUIVO_CACHE, 'rb'))
            if 'ultima_atualizacao' in cache_disco:
                self.__horario_ultima_atualizacao = cache_disco['ultima_atualizacao']
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
        if 'ultima_atualizacao' in self.__cache:
            return len(self.__lista_operacoes) >= self.NUMERO_MAX_REGISTROS + 1 # Mais um para ignorar o campo 'ultima_atualizacao'
        else:
            return len(self.__lista_operacoes) >= self.NUMERO_MAX_REGISTROS
    
    def __deletar_todas_operacoes_cache(self, operacao):
        operacoes_deletar = []
        for operacao_armazenada in self.__cache.keys():
            if operacao_armazenada.split(" ")[0] == operacao:
                operacoes_deletar.append(operacao_armazenada)
                
        if len(operacoes_deletar) > 0:
            for operacao_deletar in operacoes_deletar:
                self.__deletar_dado_cache(operacao_deletar)
                
    def __deletar_todas_operacoes_lista(self, operacao):
        for posicao, operacao_armazenada in enumerate(self.__lista_operacoes):
            if operacao_armazenada.split(" ")[0] == operacao:
                self.__lista_operacoes.pop(posicao)
    
    def __deletar_dado_cache(self, dado):
        del self.__cache[dado]
    
    def __inserir_dados_lista_operacoes(self, operacao):
        if(self.__lista_op_cheia()):
            operacao_mais_antiga = self.__lista_operacoes.pop(0)
            self.__deletar_dado_cache(operacao_mais_antiga)
            
        nome_operacao_inserir, *parametros_operacao_inserir= operacao.split(" ")
        if(nome_operacao_inserir == 'news'):
            for operacao_armazenada in self.__lista_operacoes:
                nome_operacao_armazenada, *parametros_operacao_armazenada = operacao_armazenada.split(" ")
                if nome_operacao_armazenada == nome_operacao_inserir:
                    if int(parametros_operacao_inserir[0]) <= int(parametros_operacao_armazenada[0]):
                        return
        self.__lista_operacoes.append(operacao)

    def __verificar_tempo_sincronizacao_cache(self):
        if datetime.now().timestamp() - self.__horario_ultima_atualizacao >= self.TEMPO_MIN_SINCRONIZACAO_CACHE:
            self.__horario_ultima_atualizacao = datetime.now().timestamp()
            self.escrever_cache_disco()
            self.escrever_lista_operacoes_disco()
            
    def armazenar_dados_cache(self, operacao, resultado):
        self.__inserir_dados_lista_operacoes(operacao)
        nome_operacao = operacao.split(" ")[0]
        if nome_operacao == 'news':
            self.__cache['ultima_atualizacao'] = datetime.now().timestamp()
        self.__cache[operacao] = resultado
        self.__verificar_tempo_sincronizacao_cache()

    def escrever_cache_disco(self):
        os.makedirs(os.path.dirname(self.NOME_PASTA_CACHE), exist_ok=True)
        with open(self.NOME_ARQUIVO_CACHE, 'wb') as arquivo_cache:    
            pickle.dump(self.__cache, arquivo_cache)
        
    def escrever_lista_operacoes_disco(self):
        os.makedirs(os.path.dirname(self.NOME_PASTA_CACHE), exist_ok=True)
        with open(self.NOME_LISTA_OPERACOES, 'wb') as arquivo_lista_op:    
            pickle.dump(self.__lista_operacoes, arquivo_lista_op)

    def obter_dados_em_cache(self, operacao):
        nome_operacao, *parametros_operacao = operacao.split(" ")
        if nome_operacao == 'news':
            if (datetime.now().timestamp() - self.__horario_ultima_atualizacao) >= self.TEMPO_ATUALIZACAO_CACHE_NOTICIAS:
                self.__deletar_todas_operacoes_cache(nome_operacao)
                self.__deletar_todas_operacoes_lista(nome_operacao)
                return None
            for operacao_armazenada in self.__lista_operacoes:
                nome_operacao_armazenada, *parametro_operacao_armazenada = operacao_armazenada.split(" ")
                if nome_operacao_armazenada == nome_operacao and int(parametro_operacao_armazenada[0]) > int(parametros_operacao[0]):
                    operacao = operacao_armazenada
                    break

            if operacao in self.__cache:
                return self.__cache[operacao][:int(parametros_operacao[0])]
        elif operacao in self.__cache:
            return self.__cache[operacao]
        
        return None
        

    


    

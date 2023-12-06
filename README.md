# SD2023-RPC

Sistema RPC utlizando sockets TCP que a cada semana uma nova funcionalidade será implementada.

# Atualizações

## Semana 1

Simples funções matématicas implementadas:

- Soma
- Subtração
- Divisão
- Multiplicação

## Semana 2

Mais operações e multiprocessamento implementado:

- Função para verificar se um número é primo.
- Função para mostrar números primos em um determinado range.
- Adicionado multiprocessamento em função que verifica se uma quantidade determinada de números inteiros são primos para diminuir o tempo de execução.

## Semana 3

Simples cache em memória implementado:

- Dicionário que armazena o nome da operação e os valores inseridos pelo cliente na chamada de uma operação como chave. O valor é o resultado da operação.
- Cache client-side.

## Semana 4

Cache aprimorado:

- O cache funciona em memória e em disco.
- Possuí uma constante para sincronizar o cache em memória com o cache em disco de acordo com um determinado tempo (em segundos).
- Possuí uma constante para determinar o número máximo de operações em cache. Ao chegar no número máximo de operações, as mais antigas serão descartadas.
- Sempre ao finalizar o programa, o cache é escrito em disco.

## Semana 5

Operação de webscrapping implementada:

- Busca uma quantidade x de notícias no site do https://www.ifsudestemg.edu.br/.
- Utiliza o paralelismo ao realizar o webscrapping.
- Problema com o cache: caso usuário busque 3 notícias e depois busque mais 2, o cache não retornará essas 2 notícias mesmo já tendo elas salvas em outra operação.

## Semana 6

Prolema com o cache resolvido:

- O cache consegue entender que caso ao realizar uma chamada a função de buscar notícias, o número de notícias solicitado for menor do que a quantidade de notícias que já estão em cache, deve-se retornar as notícias já armazenadas e não criar outra entrada no cache.
- Adicionada constante que diz qual o tempo limite as notícias podem ficar em cache. Caso esse tempo seja passado e uma chamada a função de buscar notícias for feita, todas as notícias que estavam em cache são removidas.

## Semana 7 

Nova arquitetura de comunicação implementada:

- Servidor de nomes adicionado. Ele é responsável por dizer quais são os ips e portas dos servidores que contêm a operação que o usuário solicitou.

- A consulta dos servidores é feita do cliente para o servidor de nomes via UDP.

- O cliente escolhe aleatoriamente dentre os servidores retornados pelo servidor de nomes em qual servidor irá se conectar.

- A conexão entre o cliente e o servidor contendo a operação do usuário é via TCP

- Essa arquitetura possibilita a distribuição dos servidores de operações.


## Semana 8

Adicionada conexão segura, nova operação e logs:

- Tanto o servidor quanto o cliente utilizam sockets seguros (trocam mensagens criptografadas) para se comunicarem, adicionando uma camada a mais de segurança.

- A função `valida_CPF(str:cpf) -> bool` foi adicionada e retorna apenas se um cpf é válido ou não.

- Agora cada operação realizada pelo cliente é inserida em um arquivo de log no servidor.

- Geração de gráficos para analisar os logs: [Ver exemplos de análises](https://colab.research.google.com/drive/1nm4EKF57k5rEnJqQwo5xSeJ_isWTjbCo?usp=sharing)